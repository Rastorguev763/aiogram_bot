from bot_commands.__init__ import*

async def convert_currency(message: types.Message):
    """
    Конвертирует валюты
    https://www.exchangerate-api.com/docs/supported-currencies
    """
    # Получить параметры конвертации от пользователя
    print(message.get_args())
    amount, from_currency, to_currency = message.text.upper().split()[1:]

    # Сформировать URL запроса к API курсов валют
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    try:
        # Отправить GET-запрос к API курсов валют
        response = requests.get(url)
        response.raise_for_status()
        
        # Преобразовать ответ в JSON-формате в словарь
        data = response.json()
        
        # Извлечь курс обмена
        exchange_rate = data['rates'][to_currency]
        
        # Выполнить конвертацию
        result = float(amount) * exchange_rate
        
        # Отправить пользователю сообщение с результатом конвертации
        await message.answer(f'{amount} {from_currency} = {result:.2f} {to_currency}')
        
    except requests.exceptions.HTTPError as e:
        lgg.error(f'Ошибка при получении курсов валют: {e}')
        await message.answer('Не удалось получить данные о курсах валют.')
    except Exception as e:
        lgg.error(f'Ошибка: {e}')
        await message.answer('Не удалось создать запрос\n'
        "- напишите команду /convert 'ДЕНЕЖНАЯ СУММА В ЦИФРАХ' 'ТЕКУЩАЯ ВАЛЮТА(ФОРМАТ БИРЖИ)' 'ВАЛЮТА В КОТОРУЮ НУЖНО ПЕРЕВЕСТИ(ФОРМАТ БИРЖИ)'")
