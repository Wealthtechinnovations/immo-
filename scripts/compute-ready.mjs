import fs from 'node:fs';
const p='.governance/tasks.json';const doc=JSON.parse(fs.readFileSync(p,'utf8'));const by=new Map(doc.tasks.map(t=>[t.id,t]));
const done=id=>by.get(id)?.status==='DONE';const candidates=doc.tasks.filter(t=>['BLOCKED','READY'].includes(t.status)&&!t.blocked_by_external_access&&(t.dependencies||[]).every(done));
console.log(JSON.stringify({ready:candidates.map(t=>({id:t.id,lot:t.lot,title:t.title}))},null,2));
