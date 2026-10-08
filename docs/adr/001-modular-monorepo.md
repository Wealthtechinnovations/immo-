# ADR-001 — Monorepo modulaire

**Décision : acceptée.** Organiser COICA en apps, packages, MCP, database, infrastructure. Les domaines métier n'importent pas les adaptateurs externes ; dépendances orientées vers le domaine. Cette structure permet web/API/workers et connecteurs indépendants sans dupliquer les invariants.
