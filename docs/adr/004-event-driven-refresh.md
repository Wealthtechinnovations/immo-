# ADR-004 — Rafraîchissement événementiel idempotent

**Décision : acceptée.** Les observations nouvelles créent snapshots/version, diff puis événements d'impact. Les traitements sont idempotents et rejouables. `source_timestamp`, `retrieved_at`, version et empreinte permettent déduplication/audit. Le terme temps réel n'est utilisé que si la source le garantit.
