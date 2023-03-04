from aiogram.types import Message, CallbackQuery
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


@dp.callback_query_handler(text="batl1vs1",state=LevelUp.battle)
async def birgaxona(call:CallbackQuery):
    await call.message.answer("Batlga kimni chaqirasiz ❓\nAccount nomini kiriting ❗",reply_markup=bekor_qilish)
    await call.message.delete()
    await LevelUp.birga_bir.set()


@dp.message_handler(state=LevelUp.birga_bir)
async def Bigacxzon(ms:Message,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    user = ms.text
    check = user_name(user)
    print(check)
    if check != "None1None2":
        about = select_users(user_id)
        sorov = f"Sizni {about[1]} 1 vs 1 chaqiryapti\nSo'rovni qabul qilasizmi\
            \nUser ID: <code>{about[0]}</code>"
        chaqir = check.split(",")
        await bot.send_message(chat_id=chaqir[2],text=sorov,reply_markup=batl1vs1_btn)
        await LevelUp.start1vs1.set()
    else:
        await ms.answer("Bunday account topilmadi ⛔")



@dp.callback_query_handler(text="uyniyman",state=LevelUp.battle)
async def rozixona(call:CallbackQuery):
    await call.message.answer("💡 Id raqamni kiriting")
    # await call.message.delete()
    await LevelUp.id_kirit.set()


@dp.message_handler(state=LevelUp.id_kirit)
async def Kiritxona(ms:Message,state:FSMContext):
    date = await state.get_data()
    user_id = date.get("user_id")
    xabar = "Battle boshlandi. Kim ko'p like yig'a olsa yutadi\
            \nLike yig'ish uchun 10 daqiqa vaqt beriladi"
    btl_id = ms.text
    try:
        user1 = select_users(user_id)[1]
        user2 = select_users(btl_id)[1]
        rek_lama = InlineKeyboardMarkup(
        inline_keyboard=[[
                InlineKeyboardButton(f"{user1}",switch_inline_query="user1"),
                InlineKeyboardButton(f"{user2}",switch_inline_query="user2")
            ],[
                InlineKeyboardButton("Bat",callback_data="orqaga")
            ]])

        await ms.answer(xabar,reply_markup=rek_lama)
        await bot.send_message(chat_id=btl_id,text=xabar,reply_markup=rek_lama)
    except:
        await ms.answer("Kiritilgan id xato\nBoshqatdan urunub ko'ring")

