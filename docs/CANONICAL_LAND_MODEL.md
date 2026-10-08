# Modèle canonique foncier

Entités : Territory, AdministrativeArea, Village, Subdivision, Block, ParcelObservation, LandRightObservation, TitleObservation, CertificateObservation, RestrictionObservation, ProtectedAreaObservation, InfrastructureObservation, Evidence, GeometryVersion, InterestArea, InterestClaim, ClaimAssessment, Conflict, Procedure, PaymentReference, Event, Alert.

Un suffixe `Observation` signifie une assertion attribuée à une source, pas une vérité fusionnée. Les relations de droit sont portées par evidence/provenance. Les claims sont dans un agrégat séparé. Toute géométrie a CRS, source, version, validité, observedAt/retrievedAt et hash lorsque disponible.
