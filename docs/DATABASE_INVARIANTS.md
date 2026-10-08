# Invariants DB

La base refuse statuts Claim/Assessment inconnus, confiance hors [0,1], géométries invalides et périodes inversées. Evidence référence toujours un `source_record`. Les observations ne sont pas fusionnées par contrainte d'unicité juridique : les conflits doivent pouvoir coexister. `OFFICIALLY_CONFIRMED` requiert en plus une validation applicative des evidence légales ; une CHECK SQL seule ne peut établir l'autorité externe.
