import requests
import sys
from functools import wraps

def log_errors_to_stdout(func):
    """Декоратор для логирования ошибок в stdout."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            sys.stdout.write(f"Ошибка запроса к API: {e}\n")
            return None
        except ValueError as e:
            sys.stdout.write(f"Ошибка парсинга JSON: {e}\n")
            return None
        except KeyError as e:
            sys.stdout.write(f"Ошибка: отсутствует ключ в данных: {e}\n")
            return None
    return wrapper

@log_errors_to_stdout
def get_currencies(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    """Получает курсы валют с использованием декоратора для логирования."""
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
            sys.stdout.write(f"Предупреждение: валюта {code} отсутствует в данных API\n")
            continue
        
        currency_info = currencies_data[code]
        result[code] = currency_info.get('Value')
    
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