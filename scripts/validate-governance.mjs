import fs from 'node:fs';
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const current=read('.governance/current.json'), tasksDoc=read('.governance/tasks.json'), deps=read('.governance/dependencies.json'), sources=read('.governance/sources.json'), cp=read('.governance/checkpoint.json');
const tasks=tasksDoc.tasks; const ids=new Set(tasks.map(t=>t.id));
const fail=[];
if(tasks.length!==tasksDoc.count) fail.push(`task count ${tasks.length} != ${tasksDoc.count}`);
if(new Set(tasks.map(t=>t.id)).size!==tasks.length) fail.push('duplicate task ids');
for(const t of tasks) for(const d of t.dependencies||[]) if(!ids.has(d)) fail.push(`${t.id}: missing dependency ${d}`);
const graph=new Map(tasks.map(t=>[t.id,t.dependencies||[]])); const temp=new Set(),done=new Set();
function visit(id){if(done.has(id))return;if(temp.has(id)){fail.push(`cycle at ${id}`);return;}temp.add(id);for(const d of graph.get(id)||[])visit(d);temp.delete(id);done.add(id)}; for(const id of ids)visit(id);
const allowed=new Set(['BLOCKED','READY','CLAIMED','IN_PROGRESS','REVIEW','DONE','FAILED','CANCELED']); for(const t of tasks)if(!allowed.has(t.status))fail.push(`${t.id}: invalid status ${t.status}`);
if(current.tasks_total!==tasks.length)fail.push('current.tasks_total mismatch'); if(!ids.has(current.next_candidate))fail.push('current.next_candidate missing'); if(!ids.has(cp.next_task_candidate))fail.push('checkpoint next candidate missing');
for(const s of sources.sources){if(!s.id||!s.status)fail.push('invalid source record');if(s.api_verified===true&&s.last_verified_at==null)fail.push(`${s.id}: verified API without timestamp`)}
const lotIds=new Set(deps.lots.map(l=>l.id));for(const l of deps.lots)for(const d of l.dependencies||[])if(!lotIds.has(d))fail.push(`${l.id}: missing lot dependency ${d}`);
if(fail.length){console.error(fail.join('\n'));process.exit(1)} console.log(`governance OK: ${tasks.length} tasks, ${deps.lots.length} lots, ${sources.sources.length} sources`);
