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
import asyncio
import requests,json

# dbs = sqlite3.connect("data/online.db")
# creat = dbs.execute("""CREATE TABLE IF NOT EXISTS Fight (name TEXT, idn INT, vaqt INT)""")

user_javobi = []


@dp.message_handler(text="⚔️ Battle",state=LevelUp.bosh_holat)
async def StartBattle(ms:Message):
    await ms.answer("Quyidagilardan birini tanlang 👇",reply_markup=inline_battle)
    await LevelUp.battle.set()


## zakovat uchun handler
@dp.callback_query_handler(text="zakovat",state=LevelUp.battle)
async def Zakvat(call:CallbackQuery):
    await call.message.answer("🤓 Zakovat o'yiniga kimni chaqirasiz\n🖍 <b>Account nomini kiriting</b> ‼\
        \n🖍 <b>Yoki kelgan ID orqali o'ynang</b>",reply_markup=bekor_qilish)
    await call.message.delete()
    user_javobi.clear()
    await LevelUp.zakovat.set()


## Bekor qilish bosilsa ishga tushadi
@dp.callback_query_handler(text="bekor",state=LevelUp.zakovat)
async def BIKOPR(call:CallbackQuery):
    await call.message.answer("Quyidagilardan birini tanlang 👇",reply_markup=inline_battle)
    await call.message.delete()
    await LevelUp.battle.set()




## kiritilgan id raqamni oluvchi funksiya
@dp.message_handler(state=LevelUp.zakovat)
async def AcountQidirish(ms:Message,state:FSMContext):
    data = await state.get_data()
    user_id = data.get("user_id")
    user_id = int(user_id)
    acount_name = ms.text
    tekshir = user_name(acount_name)
    if tekshir != "None1None2":
        about = tekshir.split(",")
        ids = int(about[2])
        await state.update_data(battle_id = ids)## Batl qiluvchini id raqamini oladi
        await bot.send_message(chat_id=ids,text=f"<b>Sizni {ms.from_user.first_name} zakovat o'yiniga chaqiryapti</b>\
            \nSo'rovni qabul qilasizmi ❓\nUser ID raqam: {user_id}",reply_markup=sorovnoma)
        await ms.answer("So'rov yuborildi ✅\nNatijasi kutilmoqda../")
    else:
        await ms.answer("Bunday account yo'q\nYoki noto'gri kiritilgan")


## bekor qilish uchun yozilgan kod
@dp.callback_query_handler(text="bekor",state=LevelUp.zakovat)
async def BekQil(call:CallbackQuery):
    await call.message.answer("Quyidagilardan tanlang 👇",reply_markup=level_up_button)
    await call.message.delete()
    await LevelUp.bosh_holat.set()


##   B o s h l a s h   u c h u n   k o d  👇
##  B o s h l a s h   u c h u n   k o d    👇
## B o s h l a s h   u c h u n   k o d      👇

@dp.callback_query_handler(text="boshlash",state=LevelUp.zakovat)
async def BOSHlandi(call:CallbackQuery,state:FSMContext):
    stdate = await state.get_data()
    user_ids = stdate.get("user_id")
    battles_id = stdate.get("battle_id")
    user_ids = int(user_ids)
    battles_id = int(battles_id)
    
    # savol uchun urls
    level = select_users(user_ids)['level'].split(",")[0]
    level = int(level)
    await call.message.answer("🎯 O'yin boshlandi 🤔")
    await bot.send_message(chat_id=battles_id,text="🎯 O'yin boshlandi 🤔\
        \n<b>Boshlash tugmasini bosing</b>",reply_markup=boshlash)
    # await asyncio.sleep(2)

    if level <= 5:
        urls = "http://aabbdd.pythonanywhere.com/quiz/easy/"
    elif level <= 10:
        urls = "http://aabbdd.pythonanywhere.com/quiz/normal/"
    else:
        urls = "http://aabbdd.pythonanywhere.com/quiz/hard/"
    respons = requests.request('GET',urls)
    data = json.loads(respons.text)
    ## tepadagi kod level bo'yicha beriladi

    tr = 0
    while tr < 5:
        tr += 1
        tasodif_api = r.choice(data)
        savol = tasodif_api["quiz"]
        tru_quiz = tasodif_api["answer"]
        update_baza("savol",tru_quiz,user_ids)
        await state.update_data(tugri = tru_quiz)
        await state.update_data(number = tr)
        nurik = await bot.send_message(chat_id=battles_id,text=f"{tr}- savol\n {savol}")
        anik = await call.message.answer(f"{tr}- savol\n{savol}")

        await LevelUp.javoblar.set()
        await asyncio.sleep(20)
        await nurik.delete()
        await anik.delete()
    
    ## Hisob kitob uchun kodlar
    update_baza("battle",sum(user_javobi),user_ids)
    await asyncio.sleep(2)
    kirgan = int(select_users(battles_id)['battle'])
    chaqirgan = int(select_users(user_ids)['battle'])

    ## Kib ko'p javob topganini hisoblash uchun 👇
    ## Kib ko'p javob topganini hisoblash uchun  👇
    if kirgan > chaqirgan:
        await call.message.answer(f"<b>Siz yutqazdingiz </b>\nHisob= {kirgan} : {chaqirgan} bo'ldi",reply_markup=inline_battle)
        await bot.send_message(chat_id=battles_id,text=f"<b> Siz yutdingiz 🎉</b>\
            \nHisob= {kirgan} : {chaqirgan} bo'ldi",reply_markup=inline_battle)
        level_up(battles_id,10)
    elif kirgan < chaqirgan:
        await call.message.answer(f"<b> Siz yutdingiz 🎉</b>\
            \nHisob= {kirgan} : {chaqirgan} bo'ldi",reply_markup=inline_battle)
        await bot.send_message(chat_id=battles_id,text=f"<b>Siz yutqazdingiz </b>\
            \nHisob= {kirgan} : {chaqirgan} bo'ldi",reply_markup=inline_battle)
        level_up(user_ids,10)
    else:
        await call.message.answer(f"Hisob = {chaqirgan} : {kirgan} \nNatija durrang bo'ldi",reply_markup=inline_battle)
        await bot.send_message(chat_id=battles_id,text=f"Hisob = {kirgan} : {chaqirgan}\
            \nNatija durrang bo'ldi",reply_markup=inline_battle)
    await LevelUp.battle.set()



## javoblar uchun yozilgan kod 👇

@dp.message_handler(state=LevelUp.javoblar)
async def JavobKeldi(ms:Message, state:FSMContext):
    date = await state.get_data()
    batle_id = date.get("battle_id")
    batle_id = int(batle_id)
    
    javob = ms.text
    tugri = date.get("tugri")
    await LevelUp.set_kutish.set()

    if javob == tugri:
        user_javobi.append(1)
        balo = await ms.answer("✅ Siz to'g'ri topdingiz ")
        await ms.delete()
        await asyncio.sleep(5)
        await balo.delete()
    else:
        bola = await ms.answer("❌ Siz xato javob berdingiz")
        await ms.delete()
        await asyncio.sleep(5)
        await bola.delete()


@dp.message_handler(state=LevelUp.set_kutish)
async def Kiritma(ms:Message):
    balo = await ms.answer("⛔ Siz javob berib bo'ldingiz")
    await ms.delete()
    await asyncio.sleep(3)
    await balo.delete()



