BEGIN;
CREATE TABLE domain_events (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), event_type text NOT NULL, aggregate_type text NOT NULL, aggregate_id text NOT NULL, idempotency_key text NOT NULL UNIQUE, occurred_at timestamptz NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), payload jsonb NOT NULL DEFAULT '{}'::jsonb);
CREATE INDEX domain_events_aggregate_idx ON domain_events(aggregate_type,aggregate_id,occurred_at);
COMMIT;
