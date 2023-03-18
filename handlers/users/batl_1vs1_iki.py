from aiogram.types import Message, CallbackQuery,InlineQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from .functions import *

from states.All_State import *
from states.Levels_state import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.level_inline import *

import random as r
import asyncio,aiogram



@dp.inline_handler(text="user1",state=LevelUp)
async def user1xona(query:InlineQuery,state:FSMContext):
    date = await state.get_data()
    userid = date.get('user_id')
    sname = select_users(userid)[1]
    msg = f"Siz <b>{sname}</b> ga like bosing"
    bosish = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton("👉 Like bosaman 👈")
        ]])