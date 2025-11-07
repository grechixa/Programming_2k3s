import requests

def get_currencies(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
    """
    Получает курсы валют из API Центробанка РФ.
    
    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR'])
        url (str): URL API (по умолчанию - курс ЦБ РФ)
    
    Returns:
        dict: Словарь с курсами валют {код: курс} или None в случае ошибки
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        currencies_data = data.get("Valute")

        result = {}
        for code in currency_codes:
            if code in currencies_data:
                currency_info = currencies_data[code]
                result[code] = currency_info.get('Value', None)
        return result

    except (requests.RequestException, ValueError, KeyError):
        return None
    
currencies = get_currencies(['USD', 'EUR', 'CNY'])
print(currencies)