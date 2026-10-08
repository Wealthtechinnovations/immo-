import fs from 'node:fs';
const d=JSON.parse(fs.readFileSync('.governance/tasks.json','utf8'));
const done=new Set(d.tasks.filter(t=>t.status==='DONE').map(t=>t.id));
const candidates=d.tasks.filter(t=>t.status==='READY'&&!t.blocked_by_external_access&&(t.dependencies||[]).every(x=>done.has(x))&&t.scope?.allowed?.length);
const task=candidates[0]??null;
console.log(JSON.stringify({task:task&&{id:task.id,title:task.title,allowed:task.scope.allowed,forbidden:task.scope.forbidden,acceptance:task.acceptance}},null,2));
