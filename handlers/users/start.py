from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
# from aiogram import Dispatcher
from datetime import datetime   

from loader import dp,bot
import sqlite3
import asyncio

from .functions import *
from .function_farm import create_farm,others_create
from keyboards.default.for_start import *
from keyboards.inline.sozlamalar import *
from states.All_State import *


# dbs = sqlite3.connect("data/malumotlar.db")
# creat = dbs.execute("""CREATE TABLE IF NOT EXISTS Users (idn INT, name TEXT,phone INT,parol TEXT , level TEXT, pul INT,kumush INT,battle INT,savol TEXT)""")

telreg = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"



@dp.message_handler(CommandStart())
async def bot_start(message:Message):
    await message.answer("Accountga kiring ‼\nYoki ro'yxatdan o'ting",reply_markup=login)
    await Register.bosh_holat.set()



## Registerni bossa ishga tushadi
@dp.callback_query_handler(text="register",state=Register.bosh_holat)
async def urjaksf(call:CallbackQuery):
    id_tekshirish = call.from_user.id
    bor_yuq = tekshirish(id_tekshirish)
    if bor_yuq == "true":
        balo = await call.message.answer("💡 Kechirasiz sizni ID raqamingizdan account ochib bo'lingan 🔕")
        await asyncio.sleep(10)
        await balo.delete()
    else:
        await call.message.answer("🖊 Accountga ism kiriting\n👮🏽‍♂️ Max belgi 12 ta ✅\
            \n👮🏽‍♂️ Faqat harflar va sonlar ✅")
        await Register.ism.set()
        await call.message.delete()


@dp.message_handler(state=Register.ism)
async def ismxona(ms:Message,state:FSMContext):
    ism = ms.text
    bormi = name_check(ism)
    if bormi:
        await state.update_data(name=ism)
        await ms.answer("📞 Telefon nomer kiriting",reply_markup=phone_uvhun)
        await Register.phone.set()
    else:
        await ms.answer("❗ Ism kiritishda xato mavjut\nBoshqatdan ism kiriting ✅")




@dp.message_handler(state=Register.phone,content_types="contact")
@dp.message_handler(state=Register.phone,regexp=telreg)
async def NomerXona(ms:Message, state:FSMContext):
    if ms.contact:
        nomer = ms.contact.phone_number
    else:
        nomer = ms.text
    await state.update_data(phone=nomer)
    await ms.answer("✅ Yoshingizni kiriting")
    await Register.age.set()


@dp.message_handler(state=Register.phone)
async def NoNomer(ms:Message):
    await ms.answer("❌ Noto'g'ri nomer kiritildi")


@dp.message_handler(state=Register.age)
async def YoshXona(ms:Message, state:FSMContext):
    info = ms.from_user
    try:
        yosh = int(ms.text)
        if yosh > 0 and yosh < 101:
            await ms.answer("🔐 Yangi parol yarating\n📌 Min belgi 8 ta \
                \n📌 Harflar, Sonlar majburiy")
            await Register.password.set()
            await state.update_data(age = ms.text)
        else:
            await ms.answer("❌ yoshingizni to'g'ri kiriting")
    except ValueError:
        await ms.answer("❌ ValueError")


@dp.message_handler(state=Register.password)
async def Taratildi(ms:Message, state:FSMContext):
    password = ms.text
    if password_check(password):
        infp = ms.from_user.id
        date = await state.get_data()
        name = date.get("name")
        phone = date.get("phone")
        create_farm(name,infp)## ferma yaratish
        others_create(infp,name)# qo'shimcha yartish
        await state.update_data(user_id = infp)

        register_account(infp,name,phone,password,)## account yaratish
        await ms.answer("📃 Siz muvofaqiyatli ro'yxatdan o'tdingiz ✅\
            \n🔧 /profile ni bosib  malumotlarni ko'rishingiz mumkin ❗",reply_markup=level_games)
        await ms.delete()
        await Games.bosh_holat.set()
    else:
        await ms.answer("Parol xato kiritildi")
