import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType

TARGET_CHAT_ID = '-1002057861700'

# Инициализация бота и диспетчера
bot = Bot(token='6783544371:AAHdDS57sGq-GMM9pQr6-22ABDEC17gcDbw')
dp = Dispatcher(bot)

# Устанавливаем уровень логирования для получения информации об ошибках
logging.basicConfig(level=logging.INFO)

# Обработчик приветственного сообщения
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    info = """   
    Приветствуем Вас!
    Направьте информацию, которую хотели бы сообщить. Все сообщения принимаются анонимно!
    ----------------------------
    Вітаємо Вас!
    Направте інформацію, яку хотіли б повідомити. Усі повідомлення приймаються анонімно!
    """
    await message.reply(info)

# Обработчик текстовых сообщений
@dp.message_handler(content_types=ContentType.TEXT)
async def text_message_handler(message: types.Message):
    # Получаем текст сообщения
    text = message.text

    # Проверяем, есть ли у пользователя фотография
    if message.photo:
        photo = message.photo[-1]
        caption = message.caption if message.caption else '-'

        # Отправляем фотографию и текст в целевой чат
        await bot.send_photo(chat_id=TARGET_CHAT_ID, photo=photo.file_id, caption=caption)
    else:
        # Отправляем только текст в целевой чат
        await bot.send_message(chat_id=TARGET_CHAT_ID, text=text)

    # Подтверждаем, что информация была отправлена успешно
    await bot.send_message(message.chat.id, 'Спасибо за предоставленную информацию! Чтобы указать что-то ещё, нажмите /start')

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)