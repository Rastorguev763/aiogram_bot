async def create_poll(message: types.Message):
    """
    Создает опрос и отправляет его в групповой чат
    """
    question = message.text.split()[1:]
    question_string = ' '.join(question)
    options = ["Да", "Нет"]
    try:
        await bot.send_poll(
            chat_id=message.chat.id,
            question=question_string,
            options=options,
            is_anonymous=False
        )
    except:
        await message.answer("Не удалось создать опрос")