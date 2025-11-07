import requests
import logging
from functools import wraps

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Вывод в консоль
        logging.FileHandler('logs/currency_errors.log')  # Запись в файл
    ]
)

def log_errors_with_logging(func):
    """Декоратор для логирования ошибок с использованием модуля logging."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            logging.error(f"Ошибка запроса к API: {e}")
            return None
        except ValueError as e:
            logging.error(f"Ошибка парсинга JSON: {e}")
            return None
        except KeyError as e:
            logging.error(f"Ошибка: отсутствует ключ в данных: {e}")
            return None
    return wrapper

@log_errors_with_logging
def get_currencies(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    """Получает курсы валют с использованием logging для логирования."""
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    
    # Проверка: есть ли курсы валют в ответе
    if 'Valute' not in data:
        raise KeyError("В ответе API отсутствуют курсы валют")
    
    currencies_data = data['Valute']
    result = {}
    
    for code in currency_codes:
        # Проверка: есть ли валюта в данных
        if code not in currencies_data:
            logging.warning(f"Валюта {code} отсутствует в данных API")
            continue
        
        currency_info = currencies_data[code]
        result[code] = currency_info.get('Value')
    
    logging.info(f"Успешно получены курсы для валют: {list(result.keys())}")
    return result

# Правильно - список валют
result1 = get_currencies(['USD', 'EUR'])  
print(result1)  # {'USD': 75.45, 'EUR': 85.12}

# Правильно - одна валюта в списке
result2 = get_currencies(['USD'])  
print(result2)  # {'USD': 75.45}

# Неправильно
result3 = get_currencies('CNY')  
print(result3)  # {'USD': 75.45}