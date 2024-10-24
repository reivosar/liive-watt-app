\c live_watt_db;

CREATE TABLE IF NOT EXISTS energy_usages (
    id SERIAL PRIMARY KEY,
    prefecture_code VARCHAR(10) NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    special_high_voltage_consumption NUMERIC, 
    special_high_voltage_retailers_count NUMERIC,
    high_voltage_consumption NUMERIC,
    high_voltage_retailers_count NUMERIC,
    low_voltage_consumption NUMERIC,
    low_voltage_special_demand NUMERIC,
    low_voltage_free_pricing NUMERIC,
    low_voltage_retailers_count NUMERIC, 
    total_consumption NUMERIC, 
    total_retailers_count NUMERIC,  
    recorded_at TIMESTAMP DEFAULT NOW(),

    CONSTRAINT fk_prefecture
        FOREIGN KEY (prefecture_code) 
        REFERENCES prefectures(code)
        ON DELETE CASCADE
);

CREATE UNIQUE INDEX idx_energy_usages_unique ON energy_usages (prefecture_code, year, month);
CREATE INDEX idx_energy_usages_year_month ON energy_usages (year, month);
