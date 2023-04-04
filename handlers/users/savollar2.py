from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot
import requests
import random as r
import json,aiogram
import asyncio

from .functions import *
from states.All_State import *
from keyboards.default.for_start import *
from keyboards.inline.sozlamalar import *
from keyboards.inline.savollar_buton import *


@dp.message_handler(text="Savollarga javoblar",state=PulTop.turlar)
async def Savollar(ms:Message):
    await ms.answer("Savollarni tanlang ❗",reply_markup=nechatlig)
    await Quizs.boshi.set()

pulls = []
tugri_javob = []



@dp.callback_query_handler(text="sakista",state=Quizs.boshi)
async def Sakistalik(call:CallbackQuery,state:FSMContext):
    pulls.clear()
    tugri_javob.clear()
    pulls.append(3)

    data = await state.get_data()
    info = int(data.get('user_id'))
    print(info,type(info),'11111111111111111111111111111111111111111')
    random_urls = "http://aabbdd.pythonanywhere.com/quiz/"
    respons = requests.request('GET',random_urls)
    date = json.loads(respons.text)
    tr = 1
    await call.message.delete()
    while tr < 9:
        await state.update_data(svtr = tr)
        tasodifiy = r.choice(date)
        savol = tasodifiy["quiz"]

        variant1=tasodifiy['option1']
        variant2=tasodifiy['option2']
        variant3=tasodifiy['option3']
        variant4=tasodifiy['option4']
        true_quiz = tasodifiy['answer']

        await state.update_data(ve1 = variant1)
        await state.update_data(ve2 = variant2)
        await state.update_data(ve3 = variant3)
        await state.update_data(ve4 = variant4)
        await state.update_data(togri = true_quiz)

        options = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(f"{variant1}",callback_data="variants1"),
            InlineKeyboardButton(f"{variant2}",callback_data="variants2"),
        ],[
            InlineKeyboardButton(f"{variant3}",callback_data="variants3"),
            InlineKeyboardButton(f"{variant4}",callback_data="variants4"),

        ]])

        await state.update_data(tugri_javob=true_quiz)
        balo = await call.message.answer(f"<b>{tr} - Savol</b>\n{savol}",reply_markup=options)
        if tr >=5:
            pulls.append(1)
        tr += 1
       
        await Quizs.beshtalik.set()
        await asyncio.sleep(5)
        try:
            await balo.delete()
        except aiogram.utils.exceptions.MessageToDeleteNotFound:
            pass
    # while tugashi binan hisoblaydi 👇
    await call.message.answer(f"✅ Siz <b>{sum(tugri_javob)} ta savol</b>ga to'g'ri javob berdingiz ❗\
        \n💰 Va <b>{sum(pulls)} $</b> yutib oldingiz ✨",reply_markup=nechatlig)
    uzi_bor = pullari(info)
    jami = uzi_bor + sum(pulls)
    update_baza('pul',jami,info)
    await Quizs.boshi.set()


##   👇 O'ntalik uchun handler 👇
##  👇  O'ntalik uchun handler  👇
## 👇   O'ntalik uchun handler   👇


@dp.callback_query_handler(text="onta",state=Quizs.boshi)
async def UchtaliK(call:CallbackQuery,state:FSMContext):
    pulls.clear()
    pulls.append(3)
    tugri_javob.clear()
    data = await state.get_data()
    info = int(data.get('user_id'))
    random_urls = "http://aabbdd.pythonanywhere.com/quiz/"
    respons = requests.request('GET',random_urls)
    date = json.loads(respons.text)
    tr = 1
    await call.message.delete()
    while tr < 11:
        await state.update_data(svtr = tr)
        tasodifiy = r.choice(date)
        savol = tasodifiy["quiz"]

        variant1=tasodifiy['option1']
        variant2=tasodifiy['option2']
        variant3=tasodifiy['option3']
        variant4=tasodifiy['option4']
        true_quiz = tasodifiy['answer']

        await state.update_data(ve1 = variant1)
        await state.update_data(ve2 = variant2)
        await state.update_data(ve3 = variant3)
        await state.update_data(ve4 = variant4)
        await state.update_data(togri = true_quiz)

        options = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(f"{variant1}",callback_data="variants1"),
            InlineKeyboardButton(f"{variant2}",callback_data="variants2"),
        ],[
            InlineKeyboardButton(f"{variant3}",callback_data="variants3"),
            InlineKeyboardButton(f"{variant4}",callback_data="variants4"),

        ]])

        await state.update_data(tugri_javob=true_quiz)
        balo = await call.message.answer(f"<b>{tr} - Savol</b>\n{savol}",reply_markup=options)
        if tr > 7:
            pulls.append(2)
        tr += 1
        
        await Quizs.beshtalik.set()
        await asyncio.sleep(5)
        try:
            await balo.delete()
        except aiogram.utils.exceptions.MessageToDeleteNotFound:
            pass
    await call.message.answer(f"✅ Siz <b>{sum(tugri_javob)} ta savol</b>ga to'g'ri javob berdingiz ❗\
        \n💰 Va <b>{sum(pulls)} $</b> yutib oldingiz ✨",reply_markup=nechatlig)
    
    uzi_bor = pullari(info)
    jami = uzi_bor + sum(pulls)
    update_baza('pul',jami,info)
    await Quizs.boshi.set()




## Variantlar uchun 👇
## Variantlar uchun  👇
## Variantlar uchun   👇
@dp.callback_query_handler(text="variants1",state=Quizs.beshtalik)
async def easdm(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    tru_quiz = date.get('togri')
    ve1 = date.get('ve1')
    savol_nomeri = date.get('svtr')
    if ve1 != tru_quiz:
        turka = await call.message.answer(f"{savol_nomeri} - savolga <b>xato javob</b> berdingiz ❌")
        await call.message.delete()
        await asyncio.sleep(3)
        await turka.delete()
    else:
        suak = await call.message.answer(f"✅ Tabriklayman {savol_nomeri} - savolga to'g'ri javob berdingiz")
        await call.message.delete()
        pulls.append(1)
        tugri_javob.append(1)
        await asyncio.sleep(3)
        await suak.delete()



@dp.callback_query_handler(text="variants2",state=Quizs.beshtalik)
async def easdm(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    tru_quiz = date.get('togri')
    ve2 = date.get('ve2')
    savol_nomeri = date.get('svtr')
    if ve2 != tru_quiz:
        turka = await call.message.answer(f"{savol_nomeri} - savolga <b>xato javob</b> berdingiz ❌")
        await call.message.delete()
        await asyncio.sleep(3)
        await turka.delete()
    else:
        suak = await call.message.answer(f"✅ Tabriklayman {savol_nomeri} - savolga to'g'ri javob berdingiz")
        await call.message.delete()
        pulls.append(1)
        tugri_javob.append(1)
        await asyncio.sleep(3)
        await suak.delete()
    
        

@dp.callback_query_handler(text="variants3",state=Quizs.beshtalik)
async def easdm(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    tru_quiz = date.get('togri')
    ve3 = date.get('ve3')
    savol_nomeri = date.get('svtr')
    if ve3 != tru_quiz:
        turka = await call.message.answer(f"{savol_nomeri} - savolga <b>xato javob</b> berdingiz ❌")
        await call.message.delete()
        await asyncio.sleep(3)
        await turka.delete()
    else:
        suak = await call.message.answer(f"✅ Tabriklayman {savol_nomeri} - savolga to'g'ri javob berdingiz")
        await call.message.delete()
        pulls.append(1)
        tugri_javob.append(1)
        await asyncio.sleep(3)
        await suak.delete()
     



@dp.callback_query_handler(text="variants4",state=Quizs.beshtalik)
async def easdm(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    tru_quiz = date.get('togri')
    ve4 = date.get('ve4')
    savol_nomeri = date.get('svtr')
    if ve4 != tru_quiz:
        turka = await call.message.answer(f"{savol_nomeri} - savolga <b>xato javob</b> berdingiz ❌")
        await call.message.delete()
        await asyncio.sleep(3)
        await turka.delete()
    else:
        suak = await call.message.answer(f"✅ Tabriklayman {savol_nomeri} - savolga to'g'ri javob berdingiz")
        await call.message.delete()
        pulls.append(1)
        tugri_javob.append(1)
        await asyncio.sleep(3)
        await suak.delete()