# Plan directeur COICA — baseline v1

| Lot | Objet | Tâches | Prérequis |
|---|---|---:|---|
| L00 | Bootstrap et gouvernance agents | 8 | — |
| L01 | Architecture et décisions ADR | 7 | L00 |
| L02 | Registre et qualification des sources | 9 | L00 |
| L03 | Modèle foncier canonique | 8 | L01, L02 |
| L04 | PostGIS et infrastructure de données | 7 | L01, L03 |
| L05 | Fédération MCP et contrats | 8 | L03, L04 |
| L06 | Connecteur SIGFU | 7 | L02, L05 |
| L07 | Connecteur SIFOR-CI et AFOR | 7 | L02, L05 |
| L08 | Connecteurs géodonnées ouvertes | 8 | L05 |
| L09 | Copernicus et télédétection | 6 | L05, L08 |
| L10 | Jumeau numérique foncier | 8 | L04, L06, L07, L08, L09 |
| L11 | Intelligence spatiale | 8 | L10 |
| L12 | Moteur de vérification d'éligibilité | 8 | L11 |
| L13 | Déclarations d'intérêt foncier | 8 | L12 |
| L14 | Événements et vérification continue | 7 | L10, L13 |
| L15 | Identité API procédures et paiements | 7 | L13 |
| L16 | Cartographie publique et administration | 10 | L11, L13, L14, L15 |
| L17 | Qualité sécurité exploitation certification | 9 | L16 |

**Total : 140 tâches.** Chaque tâche a un identifiant stable dans `.governance/tasks.json` et des dépendances explicitement référencées. Une tâche dépendante d'une autorisation institutionnelle n'est pas exécutable tant que l'accès n'est pas vérifié. Une nouvelle découverte crée une tâche enfant et, si nécessaire, un amendement versionné du DAG ; jamais de déblocage fictif.

## Jalons
M0 : baseline documentaire / gouvernance ; M1 : architecture et sources vérifiées ; M2 : modèle, infrastructure et gateway ; M3 : connecteurs effectivement autorisés ; M4 : jumeau et calcul spatial ; M5 : claims, événements et parcours API ; M6 : interfaces ; M7 : certification et lancement conditionnel.

## Priorités
L00 → L01 et L02 en parallèle → L03 → L04/L05 → L06-L09 parallélisables en périmètres isolés → L10-L13 → L14/L15 → L16 → L17. Voir le DAG machine-readable, qui fait autorité sur ce résumé.
