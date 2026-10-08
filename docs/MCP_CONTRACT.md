# Contrat MCP COICA

Capacités communes : `source.health`, `source.search`, `source.fetch`, `source.refresh`, `source.provenance`, `geo.intersections`. Réponse : source, capacité, statut, données, evidence/provenance, erreurs structurées, fraîcheur. Les statuts `UNAVAILABLE`, `UNAUTHORIZED`, `STALE`, `PARTIAL` sont distincts de `OK` avec résultat vide.

Le gateway n'invente pas une capacité absente du manifest et n'effectue aucun fallback juridique silencieux entre sources.
