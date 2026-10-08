BEGIN;
CREATE TABLE land_observations (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), kind text NOT NULL CHECK(kind IN ('ADMINISTRATIVE_AREA','VILLAGE','SUBDIVISION','BLOCK','PARCEL','LAND_RIGHT','TITLE','CERTIFICATE','RESTRICTION','PROTECTED_AREA','INFRASTRUCTURE')), source_record_uuid uuid NOT NULL REFERENCES source_records(id), geometry_version_id uuid REFERENCES geometry_versions(id), external_label text, attributes jsonb NOT NULL DEFAULT '{}'::jsonb, created_at timestamptz NOT NULL DEFAULT now());
CREATE INDEX land_observations_kind_idx ON land_observations(kind);
CREATE INDEX land_observations_source_idx ON land_observations(source_record_uuid);
COMMIT;
