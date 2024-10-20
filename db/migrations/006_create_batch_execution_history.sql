\c live_watt_db;

CREATE TYPE batch_execution_status AS ENUM ('running', 'success', 'failed');

CREATE TABLE IF NOT EXISTS batch_execution_history (
    id SERIAL PRIMARY KEY,
    batch_id INTEGER NOT NULL REFERENCES batch_management(id) ON DELETE CASCADE,
    status batch_execution_status NOT NULL DEFAULT 'running', 
    started_at TIMESTAMP DEFAULT NOW(),
    finished_at TIMESTAMP,
    message TEXT
);

ALTER TABLE batch_execution_history ALTER COLUMN status TYPE batch_execution_status USING status::text::batch_execution_status;