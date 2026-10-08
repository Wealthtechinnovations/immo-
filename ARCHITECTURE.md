# Architecture cible (proposition soumise à ADR)

UI cartographique / administration / API → moteur de claims et vérification → services spatiaux PostGIS → jumeau numérique versionné → fédération MCP → connecteurs institutionnels et ouverts. Événementiel pour rafraîchissement, détection de différences, recalcul des claims concernés et alertes.

Composants candidats : `apps/web`, `apps/api`, `apps/admin`, `apps/workers`, `packages/domain`, `packages/geo`, `packages/provenance`, `mcp/gateway`, `mcp/connectors/*`, `database/migrations`, `infrastructure/*`.

**Décisions non prises :** stack frontend/backend, broker, hébergement, authentification, paiement, fréquence d'actualisation, licences, géométries accessibles. L01 doit produire les ADR nécessaires avant implémentation.

## Flux logique
Source→autorisation→MCP→validation/normalisation→provenance→version géométrique→tests qualité→requêtes spatiales→assessment explicable→claim d'intérêt→notifications si modification. Chaque source conserve sa propre autorité ; aucune fusion silencieuse de géométries contradictoires.
