# Protocole agent — sans Codex obligatoire

Entrée : lire `00_START_HERE.md`, toutes les autorités de state, le DAG, la politique de sources, et le lot. Employer les fonctions GitHub directes si disponibles ; ne pas ouvrir Codex par défaut.

États : BLOCKED, READY, CLAIMED, IN_PROGRESS, REVIEW, DONE, FAILED, CANCELED. READY ne garantit pas prise en charge ; revalider les prérequis au moment du claim.

Concurrence : un claim requiert un identifiant effectivement exposé, un propriétaire, un périmètre, un TTL et une transition atomique validée. Les fichiers JSON versionnés ne constituent pas à eux seuls un système de verrouillage transactionnel. Tant que le mécanisme d'arbitrage n'existe pas, agents parallèles : PR séparées, revue anti-collision humaine/automatisée, pas de claim simultané sur le même domaine.

Chaque tâche : observer HEAD→lire l'autorité→affiner le contrat→déclarer scope→implémenter→tests→diff→PR→CI→revue→merge autorisé→checkpoint/handoff→READY suivant. Aucun merge automatique sans gates. Fail-closed pour identité, droits, légalités, preuves et permissions absents.
