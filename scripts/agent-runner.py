#!/usr/bin/env python3
"""One-task, one-PR governed autonomous executor. No unattended merges."""
import json, os, pathlib, subprocess, sys, urllib.request, fnmatch, datetime
ROOT=pathlib.Path('.')
def run(*args, check=True):
    return subprocess.run(args,check=check,text=True,capture_output=True)
def fail(message):
    print(message,flush=True);sys.exit(0)
selection=json.loads(pathlib.Path('selection.json').read_text())
task=selection.get('task')
if not task: fail('No READY task with satisfied dependencies; fail closed.')
key=os.getenv('OPENAI_API_KEY')
if not key: fail('COICA_AGENT_API_KEY absent; runner not activated.')
model=os.getenv('MODEL') or 'gpt-4.1-mini'
if not task.get('allowed') or not all(isinstance(v,str) and v.strip() for v in task['allowed']): fail('Missing scope')
existing=run('gh','pr','list','--state','open','--json','title,headRefName')
if any(task['id'] in x['title'] for x in json.loads(existing.stdout)): fail('Task already has an open PR')
base=run('git','rev-parse','HEAD').stdout.strip()
docs=[]
for path in ['00_START_HERE.md','LEGAL_INVARIANTS.md','AGENT_PROTOCOL.md','docs/DEFINITION_OF_DONE.md']:
    p=ROOT/path
    if p.exists(): docs.append({'path':path,'content':p.read_text()[:10000]})
request={'model':model,'input':[{'role':'system','content':'You are a governed repository coding agent. Return ONLY a JSON object with key files: array of {path,content}. Do not use markdown. Implement exactly one task; no secrets, network code, CI edits, governance edits, security weakening, or unapproved source ingestion. New or edited files must match allowed scopes. Never claim tests passed.'},{'role':'user','content':json.dumps({'task':task,'documents':docs},ensure_ascii=False)}]}
req=urllib.request.Request('https://api.openai.com/v1/responses',data=json.dumps(request).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
try:
    with urllib.request.urlopen(req,timeout=90) as response: data=json.load(response)
    output=''.join(c.get('text','') for x in data.get('output',[]) for c in x.get('content',[]) if c.get('type')=='output_text')
    proposal=json.loads(output)
except Exception as e: fail('Model call/parse failed: '+str(type(e).__name__))
files=proposal.get('files',[])
if not isinstance(files,list) or not 1<=len(files)<=8: fail('Invalid file count')
protected=['.github/**','.governance/**','scripts/agent-*','scripts/agent_runner*','LEGAL_INVARIANTS.md','package.json']
for f in files:
    path=f.get('path','');content=f.get('content')
    if not path or not isinstance(content,str) or len(content)>100000: fail('Invalid file')
    p=pathlib.PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or path.startswith('.') or any(fnmatch.fnmatch(path,x) for x in protected):fail('Protected path')
    if not any(fnmatch.fnmatch(path,pattern) or (pattern.endswith('/**') and path.startswith(pattern[:-3]+'/')) for pattern in task['allowed']):fail('Outside task scope')
    if any(fnmatch.fnmatch(path,pattern) for pattern in task.get('forbidden',[])):fail('Forbidden path')
branch='agent/'+task['id'].lower()+'-'+os.getenv('GITHUB_RUN_ID','local')
run('git','checkout','-b',branch)
for f in files:
    p=ROOT/f['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_text(f['content'])
run('git','add','--',*[f['path'] for f in files])
if run('git','diff','--cached','--quiet',check=False).returncode == 0:fail('No diff')
tests=run('npm','test',check=False)
if tests.returncode:fail('Tests failed; no PR created: '+tests.stdout[-1500:]+tests.stderr[-1500:])
run('git','-c','user.name=coica-agent[bot]','-c','user.email=coica-agent@users.noreply.github.com','commit','-m','feat(agent): '+task['id'])
run('git','push','origin',branch)
body='Governed automated proposal for '+task['id']+'\n\nScope: '+', '.join(task['allowed'])+'\n\nTests: npm test passed on runner. Requires independent review. No automatic merge.'
pr=run('gh','pr','create','--base','Server','--head',branch,'--title',task['id']+' — autonomous proposal','--body',body)
print(pr.stdout)
