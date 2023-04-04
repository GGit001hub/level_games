from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp
import sqlite3

from .functions import user_name
from keyboards.default.for_start import *
from keyboards.inline.sozlamalar import *
from states.All_State import *

xato_parol = [1,1,1,1]

@dp.callback_query_handler(text="login",state=Register.bosh_holat)
async def LOHoj(call:CallbackQuery):
    await call.message.answer("<b>Account nomini kiritng ❗</b>")
    xato_parol.clear()
    for i in range(3):
        xato_parol.append(1)
    await call.message.delete()
    await Register.login_name.set()
    

@dp.message_handler(state=Register.login_name)
async def IsnTekshir(ms:Message,state:FSMContext):
    data = user_name(ms.text).split(",")
    print(data)
    if data[0] != "None1None2":
        # print(data[0])
        ismi = data[0]
        pasoword = data[1]
        id_raqam = data[2]
        await state.update_data(insd = id_raqam)
        await state.update_data(name = ismi)
        await state.update_data(parol = pasoword)
        
        await ms.answer("🔒 Parolni kiriting ❗")
        await Register.login_password.set()
    else:
        await ms.answer("❌ Bunday account yo'q",reply_markup=login)
        await Register.bosh_holat.set()



@dp.message_handler(state=Register.login_password)
async def Paswords(ms:Message, state:FSMContext):
    date = await state.get_data()
    passworks = date.get("parol")
    kiritilgan_parol = ms.text
    id_raqam = date.get("insd")
    nomi = date.get("name")

    if kiritilgan_parol == passworks:
        await ms.answer(f"<b>Xush kelipsiz</b> {nomi}\n/profile malumotlarni tekshirish")
        await state.update_data(user_id = id_raqam)
        await ms.delete()
        await Games.bosh_holat.set()
    elif sum(xato_parol) == 0:
        await ms.answer("Accountga kiring ‼\nYoki ro'yxatdan o'ting",reply_markup=login)
        await Register.bosh_holat.set()
    else:
        await ms.answer(f"Noto'g'ri parol ❌\nUrunishlar soni: {sum(xato_parol)} ta")
        xato_parol.remove(1)