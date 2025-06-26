import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties  # ✅ Вот это добавили

# 🔐 Токен бота
import os

TOKEN = os.getenv("BOT_TOKEN")


# 🧱 Инициализация бота
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # ✅ Здесь убрали types.
)

dp = Dispatcher()

# 🔘 Кнопки
def get_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="📦 Скачать дизайнерский пак", url="https://your-pack-link.com")
    builder.button(text="🌐 VK", url="https://vk.com/yourprofile")
    builder.button(text="📸 Instagram", url="https://instagram.com/yourprofile")
    builder.button(text="🎬 YouTube", url="https://youtube.com/@yourchannel")
    builder.adjust(1)
    return builder.as_markup()

# 🚀 /start
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        f"<b>Привет, {message.from_user.first_name}!</b>\n\n"
        "Вот твой дизайнерский пак и полезные ссылки 👇",
        reply_markup=get_main_keyboard()
    )

# 🔁 Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

