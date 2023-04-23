from bot_commands.__init__ import*
async def send_random_animal_pic(message: types.Message):
    """
    Отправляет случайную картинку с милым животным
    """
    animal_list = ['bird', 'cat', 'dog', 'fox', 'kangaroo', 'koala', 'panda', 'raccoon', 'red panda']
    animal = random.choice(animal_list)
  
    try:
        response = requests.get(f"https://some-random-api.ml/img/{animal}")
        pic_url = json.loads(response.text)["link"]
        await message.answer_photo(pic_url)
    except:
        await message.answer("Не удалось отправить картинку")