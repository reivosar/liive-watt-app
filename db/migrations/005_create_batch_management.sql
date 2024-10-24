\c live_watt_db;

CREATE TYPE batch_management_status AS ENUM ('active', 'inactive');

CREATE TABLE IF NOT EXISTS batch_management (
    id SERIAL PRIMARY KEY,
    batch_name VARCHAR(255) NOT NULL,
    module_path VARCHAR(255) NOT NULL,
    class_name VARCHAR(255),
    function_name VARCHAR(255) NOT NULL,
    status batch_management_status NOT NULL DEFAULT 'active',
    last_run_at TIMESTAMP
);

CREATE UNIQUE INDEX idx_batch_management_batch_name ON batch_management (batch_name);

ALTER TABLE batch_management ALTER COLUMN status TYPE batch_management_status USING status::text::batch_management_status;

INSERT INTO batch_management (batch_name, module_path, class_name, function_name, status, last_run_at)
VALUES 
('electricity_data_import', 'app.jobs.electricity_data_import.runner', 'ElectricityDataImport', 'run', 'active', NOW());