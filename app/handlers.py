from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.formatting import Text, Bold

import app.keyboards as kb
#from app.database.requests import get_product



router = Router()


# Хэндлер на команду /start
@router.message(CommandStart())
async def cmd_start(message:Message):
    content = Text(
        'Добро пожаловать! ', Bold(message.from_user.full_name), ' Это бот напоминаний!'
    )
    await message.answer(
        **content.as_kwargs()
    )