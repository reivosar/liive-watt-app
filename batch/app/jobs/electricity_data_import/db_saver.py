from app.db.models.energy_usage import EnergyUsage
from app.db.models.prefecture import Prefecture
from sqlalchemy.orm import Session
from sqlalchemy import text 
from app.db.connection import session_scope
import math

class DBSaver:
    def __init__(self):
        self.prefecture_cache = {}

    def save_to_db(self, extracted_data):
        print("Starting to save data to the database")
        try:
            with session_scope() as db:
                self.load_prefecture_cache(db)
                self.save_to_energy_usages(db, extracted_data)
                db.commit()
                print("Database commit completed")
                return True
        except Exception as e:
            db.rollback()
            print(f"An error occurred during the batch job: {e}")
            return False
        finally:
            print("Finished to save data to the database.")

    def save_to_energy_usages(self, db, extracted_data):
        for record in extracted_data:
            try :
                prefecture_code = self.get_prefecture_code(record['prefecture_name'])
                    
                if not prefecture_code:
                    raise ValueError(f"Prefecture code not found for {record['prefecture_name']}")

                if self.is_nan(prefecture_code):
                    print(f"Warning: Prefecture code is NaN for {record['prefecture_name']}. Skipping record.")
                    continue
                        
                db.execute(
                    text(
                        """
                        INSERT INTO energy_usages (
                            prefecture_code, year, month, 
                            special_high_voltage_consumption, special_high_voltage_retailers_count,
                            high_voltage_consumption, high_voltage_retailers_count, 
                            low_voltage_consumption, low_voltage_special_demand, 
                            low_voltage_free_pricing, low_voltage_retailers_count,
                            total_consumption, total_retailers_count
                        )
                        VALUES (
                            :prefecture_code, :year, :month,
                            :special_high_voltage_consumption, :special_high_voltage_retailers_count,
                            :high_voltage_consumption, :high_voltage_retailers_count,
                            :low_voltage_consumption, :low_voltage_special_demand,
                            :low_voltage_free_pricing, :low_voltage_retailers_count,
                            :total_consumption, :total_retailers_count
                        )
                        ON CONFLICT (prefecture_code, year, month)
                        DO UPDATE SET
                            special_high_voltage_consumption = EXCLUDED.special_high_voltage_consumption,
                            special_high_voltage_retailers_count = EXCLUDED.special_high_voltage_retailers_count,
                            high_voltage_consumption = EXCLUDED.high_voltage_consumption,
                            high_voltage_retailers_count = EXCLUDED.high_voltage_retailers_count,
                            low_voltage_consumption = EXCLUDED.low_voltage_consumption,
                            low_voltage_special_demand = EXCLUDED.low_voltage_special_demand,
                            low_voltage_free_pricing = EXCLUDED.low_voltage_free_pricing,
                            low_voltage_retailers_count = EXCLUDED.low_voltage_retailers_count,
                            total_consumption = EXCLUDED.total_consumption,
                            total_retailers_count = EXCLUDED.total_retailers_count,
                            recorded_at = NOW()
                        """
                    ),
                    {
                        'prefecture_code': prefecture_code,
                        'year': record['year'],
                        'month': record['month'],
                        'special_high_voltage_consumption': record['special_high_voltage_consumption'],
                        'special_high_voltage_retailers_count': record['special_high_voltage_retailers_count'],
                        'high_voltage_consumption': record['high_voltage_consumption'],
                        'high_voltage_retailers_count': record['high_voltage_retailers_count'],
                        'low_voltage_consumption': record['low_voltage_consumption'],
                        'low_voltage_special_demand': record['low_voltage_special_demand'],
                        'low_voltage_free_pricing': record['low_voltage_free_pricing'],
                        'low_voltage_retailers_count': record['low_voltage_retailers_count'],
                        'total_consumption': record['total_consumption'],
                        'total_retailers_count': record['total_retailers_count']
                    }
                )
            except Exception as e:
                print(f"An error occurred during the batch job: {e} | Record: {record}")

    def load_prefecture_cache(self, db: Session):
        prefectures = db.query(Prefecture).all()
        self.prefecture_cache = {prefecture.name: prefecture.code for prefecture in prefectures}

    def get_prefecture_code(self, prefecture_name: str):
        if not prefecture_name or prefecture_name.lower() == 'nan':
            return None
        return self.prefecture_cache.get(prefecture_name)
    
    def is_nan(self, value):
        try:
            return math.isnan(float(value))
        except:
            return False