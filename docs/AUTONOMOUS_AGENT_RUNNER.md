# Autonomous coding runner — guarded
Le workflow `autonomous-agent.yml` est un exécuteur GitHub Actions planifié toutes les six heures. Il lit une seule tâche READY dont les dépendances sont DONE, refuse les accès externes non autorisés, appelle un modèle via API, limite strictement les fichiers au scope déclaré, exécute `npm test`, puis ouvre une PR. **Il ne fusionne jamais seul**, ne modifie pas les autorités de gouvernance et ne peut pas exécuter une tâche sans contrat de scope.

## Activation
Un propriétaire du dépôt doit configurer le secret Actions `COICA_AGENT_API_KEY` avec une clé API valide et, facultativement, la variable `COICA_AGENT_MODEL`. La clé ne doit jamais être committée. Sans ce secret, le runner sort proprement sans mutation. Les politiques de sécurité GitHub Actions et les permissions de création de PR doivent permettre l'action.

## Limites
Le workflow programmé n'est pas une session ChatGPT persistante. La concurrence GitHub Actions sérialise les exécutions de ce workflow, mais ne remplace pas un verrou transactionnel inter-providers. Aucune tâche READY ne sera fabriquée automatiquement : l'état de gouvernance doit être corrigé et approuvé par un chemin gouverné. Les PR générées nécessitent revue indépendante et contrôles CI avant fusion. L'appel modèle peut générer du code incorrect ; les tests ne sont pas une preuve de sécurité complète.
