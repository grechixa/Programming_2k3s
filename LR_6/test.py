import unittest
from io import StringIO
import sys
from iter3 import get_currencies

class TestGetCurrencies(unittest.TestCase):
    
    def test_successful_response(self):
        """Проверка успешного получения курсов."""
        result = get_currencies(['USD', 'EUR'])
        self.assertIsInstance(result, dict)
        self.assertIn('USD', result)
        self.assertIn('EUR', result)
        self.assertIsInstance(result['USD'], float)
    
    def test_missing_currency(self):
        """Проверка обработки отсутствующей валюты."""
        result = get_currencies(['USD', 'XYZ'])
        self.assertIn('USD', result)
        self.assertNotIn('XYZ', result)
    
    def test_api_error(self):
        """Проверка обработки ошибки API."""
        result = get_currencies(['USD'], "https://invalid-url.com")
        self.assertIsNone(result)
    
    def test_log_output(self):
        """Проверка записи логов."""
        with self.assertLogs(level='WARNING') as log:
            get_currencies(['XYZ'])  # Несуществующая валюта
            self.assertIn('XYZ', str(log.output))

if __name__ == '__main__':
    unittest.main()