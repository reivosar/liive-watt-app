import unittest
from unittest.mock import MagicMock, patch
from app.jobs.electricity_data_import.db_saver import DBSaver
from app.db.models.prefecture import Prefecture

class TestSaveToDB(unittest.TestCase):
    @patch('app.jobs.electricity_data_import.db_saver.session_scope')
    def test_save_to_db_success(self, mock_session_scope):
        # Given
        mock_session = MagicMock()
        mock_session_scope.return_value.__enter__.return_value = mock_session
        db_saver = DBSaver()
        db_saver.prefecture_cache = {'北海道': '01'}
        extracted_data = [
            {
                'prefecture_name': '北海道',
                'year': 2020,
                'month': 4,
                'special_high_voltage_consumption': 1000,
                'special_high_voltage_retailers_count': 10,
                'high_voltage_consumption': 2000,
                'high_voltage_retailers_count': 20,
                'low_voltage_consumption': 3000,
                'low_voltage_special_demand': 4000,
                'low_voltage_free_pricing': 5000,
                'low_voltage_retailers_count': 30,
                'total_consumption': 6000,
                'total_retailers_count': 40
            }
        ]
        mock_session.execute = MagicMock()

        # When
        result = db_saver.save_to_db(extracted_data)

        # Then
        mock_session.execute.assert_called_once()
        self.assertTrue(result)
        mock_session.commit.assert_called_once()

    @patch('app.jobs.electricity_data_import.db_saver.session_scope')
    def test_save_to_db_failure(self, mock_session_scope):
        # Given
        mock_session = MagicMock()
        mock_session_scope.return_value.__enter__.return_value = mock_session
        db_saver = DBSaver()
        db_saver.prefecture_cache = {'北海道': '01'}
        extracted_data = [
            {
                'prefecture_name': '北海道',
                'year': 2020,
                'month': 4,
                'special_high_voltage_consumption': 1000,
                'special_high_voltage_retailers_count': 10,
                'high_voltage_consumption': 2000,
                'high_voltage_retailers_count': 20,
                'low_voltage_consumption': 3000,
                'low_voltage_special_demand': 4000,
                'low_voltage_free_pricing': 5000,
                'low_voltage_retailers_count': 30,
                'total_consumption': 6000,
                'total_retailers_count': 40
            }
        ]
        mock_session.execute.side_effect = Exception("DB execution error")

        # When
        result = db_saver.save_to_db(extracted_data)

        # Then
        self.assertFalse(result)
        mock_session.rollback.assert_called_once()

class TestSaveToEnergyUsages(unittest.TestCase):
    def setUp(self):
        self.db_saver = DBSaver()
        self.mock_session = MagicMock()

    def test_save_to_energy_usages_success(self):
        # Given
        extracted_data = [
            {
                'prefecture_name': '北海道',
                'year': 2020,
                'month': 4,
                'special_high_voltage_consumption': 1000,
                'special_high_voltage_retailers_count': 10,
                'high_voltage_consumption': 2000,
                'high_voltage_retailers_count': 20,
                'low_voltage_consumption': 3000,
                'low_voltage_special_demand': 4000,
                'low_voltage_free_pricing': 5000,
                'low_voltage_retailers_count': 30,
                'total_consumption': 6000,
                'total_retailers_count': 40
            }
        ]
        self.db_saver.prefecture_cache = {'北海道': '01'}
        self.mock_session.execute = MagicMock()

        # When
        self.db_saver.save_to_energy_usages(self.mock_session, extracted_data)

        # Then
        self.mock_session.execute.assert_called_once()

    def test_save_to_energy_usages_missing_prefecture_code(self):
        # Given
        extracted_data = [
            {
                'prefecture_name': '不明',
                'year': 2020,
                'month': 4,
                'special_high_voltage_consumption': 1000,
                'special_high_voltage_retailers_count': 10,
                'high_voltage_consumption': 2000,
                'high_voltage_retailers_count': 20,
                'low_voltage_consumption': 3000,
                'low_voltage_special_demand': 4000,
                'low_voltage_free_pricing': 5000,
                'low_voltage_retailers_count': 30,
                'total_consumption': 6000,
                'total_retailers_count': 40
            }
        ]
        self.db_saver.prefecture_cache = {'北海道': '01'}
        
        # When
        self.db_saver.save_to_energy_usages(self.mock_session, extracted_data)

        # Then
        self.mock_session.execute.assert_not_called()

class TestLoadPrefectureCache(unittest.TestCase):
    def setUp(self):
        self.db_saver = DBSaver()
        self.mock_session = MagicMock()

    def test_load_prefecture_cache_success(self):
        # Given
        mock_prefectures = [
            Prefecture(name='北海道', code='01'),
            Prefecture(name='青森県', code='02')
        ]

        self.mock_session.query.return_value.all.return_value = mock_prefectures

        # When
        self.db_saver.load_prefecture_cache(self.mock_session)

        # Then
        self.assertEqual(self.db_saver.prefecture_cache, {'北海道': '01', '青森県': '02'})

class TestGetPrefectureCode(unittest.TestCase):
    def setUp(self):
        self.db_saver = DBSaver()
        self.db_saver.prefecture_cache = {'北海道': '01', '青森県': '02'}

    def test_get_prefecture_code_success(self):
        # Given / When
        prefecture_code = self.db_saver.get_prefecture_code('北海道')

        # Then
        self.assertEqual(prefecture_code, '01')

    def test_get_prefecture_code_nan(self):
        # Given / When
        prefecture_code = self.db_saver.get_prefecture_code('nan')

        # Then
        self.assertIsNone(prefecture_code)

class TestIsNan(unittest.TestCase):
    def setUp(self):
        self.db_saver = DBSaver()

    def test_is_nan_true(self):
        # Given / When
        result = self.db_saver.is_nan(float('nan'))

        # Then
        self.assertTrue(result)

    def test_is_nan_false(self):
        # Given / When
        result = self.db_saver.is_nan(123)

        # Then
        self.assertFalse(result)
