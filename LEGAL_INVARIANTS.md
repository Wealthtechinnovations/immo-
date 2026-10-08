# Invariants juridiques et d'interface — non négociables

- NO_DATA != NO_RIGHTS
- NOT_LOTTED != AVAILABLE
- ABSENCE_OF_PARCEL != PUBLIC_DOMAIN
- PHYSICAL_VACANCY != LEGAL_VACANCY
- INTEREST_CLAIM != OWNERSHIP
- SATELLITE_OBSERVATION != CADASTRAL_TITLE
- COICA_SCORE != LEGAL_DECISION
- PAYMENT != LAND_ACQUISITION

Les verdicts incluent UNKNOWN, INSUFFICIENT_DATA, KNOWN_CONFLICT, RESTRICTED, UNDER_REVIEW, POTENTIALLY_ELIGIBLE, ELIGIBLE_FOR_PROCEDURE, OFFICIALLY_CONFIRMED. Ce dernier exige preuve probante d'une autorité habilitée. Les claims d'intérêt ne créent pas de droit réel ; les interfaces doivent le montrer sans ambiguïté.

Critères QA négatifs obligatoires : aucune transition inférée NO_DATA→AVAILABLE, NOT_LOTTED→PURCHASABLE, CLAIM→TITLE, SATELLITE_EMPTY→FREE_LAND.
