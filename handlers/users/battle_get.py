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

user_javobi = []

## orqaga qaytish uchun kod
@dp.callback_query_handler(text="orqaga",state=LevelUp.battle)
async def Orqadka(call:CallbackQuery):
    await call.message.answer("Quyidagilardan tanlang 👇",reply_markup=level_up_button)
    await call.message.delete()
    await LevelUp.bosh_holat.set()

@dp.callback_query_handler(text="albatta",state=LevelUp.zakovat)
async def Albatta(call:CallbackQuery):
    await call.message.answer("User ID raqamini kiriting !")
    await call.message.delete()
    user_javobi.clear()
    await LevelUp.id_olish.set()


@dp.message_handler(state=LevelUp.id_olish)
async def Sdaklaf(ms:Message,state:FSMContext):
    get_id = ms.text
    try:
        await bot.send_message(chat_id=get_id,text="User  so'rovni qabul qildi\
            \nBoshlash tugmasini bosing ❗",reply_markup=boshlash)
        await state.update_data(idn_get = get_id)
        await LevelUp.join_zkv.set()
    except ValueError:
        await ms.answer("ID raqam mavjut emas\nYoki xato kiritilgan")




@dp.callback_query_handler(text="boshlash",state=LevelUp.join_zkv)
async def ZakVat(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    battle_id = date.get("idn_get")
    user_idn = date.get("user_id")
    await call.message.delete()
    await asyncio.sleep(2)

    tr = 0
    while tr < 5:
        tr += 1
        tugri = select_users(battle_id)[8]
        await state.update_data(number = tr)
        await LevelUp.get_javob.set()

        await asyncio.sleep(25)
    
    update_baza("battle",sum(user_javobi),user_idn)
    # await call.message.answer("O'yin tugadi \nNatijalar hisoblanmoqda...")
    await LevelUp.battle.set()




## javoblar uchun handler dodown 
@dp.message_handler(state=LevelUp.get_javob)
async def MKSO(ms:Message,state:FSMContext):
    date = await state.get_data()
    battle_id = date.get("idn_get")
    javob = ms.text
    tugri = select_users(battle_id)[8]

    await LevelUp.get_kutish.set()
    if javob == tugri:
        user_javobi.append(1)
        bola = await ms.answer("✅ Siz to'g'ri javob berdingiz")
        await ms.delete()
        await asyncio.sleep(5)
        await bola.delete()
    else:
        balo = await ms.answer("❌ Siz xato javob berdingiz")
        await ms.delete()
        await asyncio.sleep(5)
        await balo.delete()



# javob bersa kutish rejimiga o'tadi
@dp.message_handler(state=LevelUp.get_kutish)
async def KIRITma(ms:Message):
    balo = await ms.answer("⛔ Siz javob berib bo'ldingiz")
    await ms.delete()
    await asyncio.sleep(3)
    await balo.delete()