from bot_commands.__init__ import*
from bot_commands.convert_currency import*
from bot_commands.create_poll import*
from bot_commands.get_weather import*
from bot_commands.send_random_animal_pic import*
from bot_commands.start import*

# Настраиваем логирование
lgg.basicConfig(level=lgg.INFO)

# Регистрируем функции в диспетчере

dp.register_message_handler(start, commands=['start', 's'])
dp.register_message_handler(get_weather, commands=['weather', 'w'])
dp.register_message_handler(convert_currency, commands=['convert', 'c'])
dp.register_message_handler(send_random_animal_pic, commands=['pic', 'p'])
dp.register_message_handler(create_poll, commands=['poll'])

# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)