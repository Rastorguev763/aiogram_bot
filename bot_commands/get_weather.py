from bot_commands.__init__ import*
API_KEY = os.environ.get("API_WEATHER_TOKEN")

# Функция для получения текущей погоды
async def get_weather(message: types.Message):
    """
    Получает текущую погоду в городе
    """
    # Получить название города от пользователя
    city = message.text.split()[1]
    # Сформировать URL запроса к API погоды
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        # Отправить GET-запрос к API погоды
        response = requests.get(url)
        response.raise_for_status()
        
        # Преобразовать ответ в JSON-формате в словарь
        data = response.json()
        
        # Извлечь нужные данные о погоде
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        # Отправить пользователю сообщение о погоде
        await message.answer(f'Текущая температура в городе {city}: {temp}°C\n'
                            f'Ощущается как: {feels_like}°C\n'
                            f"Влажность: {humidity}%\n"
                            f'Описание погоды: {description}')
        
    except requests.exceptions.HTTPError as e:
        lgg.error(f'Ошибка при получении погоды: {e}')
        await message.answer(f'Не удалось получить данные о погоде в городе {city}.')
    except Exception as e:
        lgg.error(f'Ошибка: {e}')
        await message.answer('Не удалось создать запрос\n'
                                     "- напишите команду /weather 'НАЗВАНИЕ ГОРОДА'")
