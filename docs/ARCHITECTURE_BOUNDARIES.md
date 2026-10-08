# Frontières d'architecture

`domain` : invariants et modèles sans réseau/DB. `application` : use cases et ports. `geo` : types/algorithmes spatiaux purs. `provenance` : observations/evidence. `adapters` : DB/HTTP/MCP. `apps` : composition. `mcp/connectors` : accès source isolé. `database` : migrations, pas de logique juridique cachée.

Interdit : frontend décidant seul de claimability ; connecteur écrivant directement un claim ; satellite créant un droit ; paiement changeant ownership ; source sans provenance ; dépendance domaine→adapter.
