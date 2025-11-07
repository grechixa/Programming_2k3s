import requests
import sys

def get_currencies(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    """
    Получает курсы валют с обработкой исключений и логированием в stdout.
    """
    # Проверка типа входного параметра
    if isinstance(currency_codes, str):
        sys.stdout.write("Предупреждение: currency_codes должна быть списком[], а не строкой''. Преобразую в список.\n")
        currency_codes = [currency_codes]
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        # Проверка: есть ли курсы валют в ответе
        if 'Valute' not in data:
            sys.stdout.write("Ошибка: в ответе API отсутствуют курсы валют\n")
            return None
        
        currencies_data = data['Valute']
        result = {}
        
        for code in currency_codes:
            # Проверка: есть ли валюта в данных
            if code not in currencies_data:
                sys.stdout.write(f"Ошибка: валюта {code} отсутствует в данных API\n")
                continue
            
            currency_info = currencies_data[code]
            result[code] = currency_info.get('Value')
        
        return result
        
    except requests.RequestException as e:
        sys.stdout.write(f"Ошибка запроса к API: {e}\n")
        return None
    except ValueError as e:
        sys.stdout.write(f"Ошибка парсинга JSON: {e}\n")
        return None
    
print(get_currencies('USD'))