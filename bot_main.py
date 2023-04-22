import logging as lgg
from aiogram import Bot, Dispatcher, types, executor
import requests, json, random, os
from dotenv import load_dotenv
load_dotenv()

# Установить токен бота и апи погоды
TOKEN = os.environ.get("TLG_BOT_TOKEN")
API_KEY = os.environ.get("API_WEATHER_TOKEN")

# Настраиваем логирование
lgg.basicConfig(level=lgg.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функция для приветствия пользователя и предложения выбрать опцию
async def start(message: types.Message):
    """
    Приветствует пользователя и предлагает ему выбрать опцию
    """
    await message.answer(
        "Привет! Я могу выполнить следующие задачи:\n"
        "1. Узнать текущую погоду в городе\n"
        "- напишите команду /weather 'НАЗВАНИЕ ГОРОДА'\n"
        "2. Конвертировать валюты\n"
        "- напишите команду /convert 'ДЕНЕЖНАЯ СУММА В ЦИФРАХ' 'ТЕКУЩАЯ ВАЛЮТА(ФОРМАТ БИРЖИ)' 'ВАЛЮТА В КОТОРУЮ НУЖНО ПЕРЕВЕСТИ(ФОРМАТ БИРЖИ)'\n"
        "3. Отправить милую картинку\n"
        "- напишите команду /pic\n"
        "4. Создать опрос\n"
        "- напишите команду /poll 'НАЗВАНИЕ ОПРОСА: ответ ДА, ответ НЕТ'"
    )

# # Функция для получения текущей погоды
# async def get_weather(message: types.Message):
#     """
#     Получает текущую погоду в городе
#     """
#     # Получить название города от пользователя
#     city = message.text.split()[1]
#     # Сформировать URL запроса к API погоды
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

#     try:
#         # Отправить GET-запрос к API погоды
#         response = requests.get(url)
#         response.raise_for_status()
        
#         # Преобразовать ответ в JSON-формате в словарь
#         data = response.json()
        
#         # Извлечь нужные данные о погоде
#         temp = data['main']['temp']
#         feels_like = data['main']['feels_like']
#         humidity = data['main']['humidity']
#         description = data['weather'][0]['description']
        
#         # Отправить пользователю сообщение о погоде
#         await message.answer(f'Текущая температура в городе {city}: {temp}°C\n'
#                             f'Ощущается как: {feels_like}°C\n'
#                             f"Влажность: {humidity}%\n"
#                             f'Описание погоды: {description}')
        
#     except requests.exceptions.HTTPError as e:
#         lgg.error(f'Ошибка при получении погоды: {e}')
#         await message.answer(f'Не удалось получить данные о погоде в городе {city}.')
#     except Exception as e:
#         lgg.error(f'Ошибка: {e}')
#         await message.answer('Произошла ошибка при выполнении запроса. Попробуйте позже.')
# Функция для конвертации валют
# async def convert_currency(message: types.Message):
#     """
#     Конвертирует валюты
#     https://www.exchangerate-api.com/docs/supported-currencies
#     """
#     # Получить параметры конвертации от пользователя
#     amount, from_currency, to_currency = message.text.split()[1:]

#     # Сформировать URL запроса к API курсов валют
#     url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

#     try:
#         # Отправить GET-запрос к API курсов валют
#         response = requests.get(url)
#         response.raise_for_status()
        
#         # Преобразовать ответ в JSON-формате в словарь
#         data = response.json()
        
#         # Извлечь курс обмена
#         exchange_rate = data['rates'][to_currency]
        
#         # Выполнить конвертацию
#         result = float(amount) * exchange_rate
        
#         # Отправить пользователю сообщение с результатом конвертации
#         await message.answer(f'{amount} {from_currency} = {result:.2f} {to_currency}')
        
#     except requests.exceptions.HTTPError as e:
#         lgg.error(f'Ошибка при получении курсов валют: {e}')
#         await message.answer('Не удалось получить данные о курсах валют.')
#     except Exception as e:
#         lgg.error(f'Ошибка: {e}')
#         await message.answer('Произошла ошибка при выполнении запроса. Попробуйте позже.')
# Функция для отправки случайной картинки с животными
# async def send_random_animal_pic(message: types.Message):
#     """
#     Отправляет случайную картинку с милым животным
#     """
#     animal_list = ['bird', 'cat', 'dog', 'fox', 'kangaroo', 'koala', 'panda', 'raccoon', 'red panda']
#     animal = random.choice(animal_list)
  
#     try:
#         response = requests.get(f"https://some-random-api.ml/img/{animal}")
#         pic_url = json.loads(response.text)["link"]
#         await message.answer_photo(pic_url)
#     except:
#         await message.answer("Не удалось отправить картинку")

# Функция для создания опроса
# async def create_poll(message: types.Message):
#     """
#     Создает опрос и отправляет его в групповой чат
#     """
#     question = message.text.split()[1:]
#     question_string = ' '.join(question)
#     options = ["Да", "Нет"]
#     try:
#         await bot.send_poll(
#             chat_id=message.chat.id,
#             question=question_string,
#             options=options,
#             is_anonymous=False
#         )
#     except:
#         await message.answer("Не удалось создать опрос")

# Регистрируем функции в диспетчере

dp.register_message_handler(start, commands=['start'])
dp.register_message_handler(get_weather, commands=['weather'])
dp.register_message_handler(convert_currency, commands=['convert'])
dp.register_message_handler(send_random_animal_pic, commands=['pic'])
dp.register_message_handler(create_poll, commands=['poll'])
# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)