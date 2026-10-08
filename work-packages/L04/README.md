# L04 — PostgreSQL/PostGIS

Objectif : matérialiser le stockage versionné et provenance-first. Cette migration crée le noyau spatial, pas un cadastre souverain. SRID de stockage canonique : EPSG:4326 ; les calculs de surface doivent utiliser `geography` ou une projection adaptée documentée.
