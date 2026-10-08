# Point d’entrée obligatoire — COICA

1. Identifier le dépôt, la branche et le HEAD réellement exposés ; ne jamais inventer d'identité provider/session.
2. Lire `CURRENT_STATE.md`, `.governance/current.json`, `.governance/tasks.json`, `.governance/dependencies.json`, `.governance/checkpoint.json` et `.governance/handoff.json`.
3. Lire `LEGAL_INVARIANTS.md`, `SOURCE_POLICY.md`, `AGENT_PROTOCOL.md`, `ARCHITECTURE.md` et la documentation liée au lot.
4. Calculer les tâches READY à partir du DAG ; aucune tâche n'est acquise uniquement parce qu'elle apparaît READY.
5. Vérifier le claim/lease et les droits sur le périmètre ; faute de mécanisme atomique ou d'identité exposée, rester en attente et demander résolution via PR, sans fabrication de lease.
6. Traiter une tâche à la fois, sur branche de travail gouvernée ; CI, PR, contrôle diff et anti-régression avant clôture.
7. Écrire le handoff/checkpoint et mettre à jour état, historique et prochaines actions.

La présence du dépôt dans GitHub ne prouve aucune admission à une gouvernance externe GSCC/GSE/GACR ; ce projet est autonome et ne revendique pas l'implémentation de ce workflow.
