from aiogram.types import Message, CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from .functions import *
from .function_farm import *

from states.All_State import *
from states.Levels_state import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.savdo_button import *

import random as r
import asyncio,aiogram



@dp.callback_query_handler(text="quyon1x",state=Marketnig.fermas)
async def fermaxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    about_user = select_users(user_idn)
    about_farm = select_users_farm(user_idn)
 
    kumush = about_user[6]
    bor_quyon = about_farm[2]

    if kumush >= 15:
        gems = int(kumush) - 15
        get = int(bor_quyon) + 1
        update_farm("quyon",get,user_idn)
        update_baza("kumush",gems,user_idn)
        await call.message.answer(f"🐰 bitta quyon sotib olindi \
            \n✅ Sizda {get} ta quyon bor",reply_markup=ichiga_kir)
        await call.message.delete()
        level_up(user_idn,7)
        await Marketnig.ichiga.set()

    else:
        tagmadi = await call.message.answer("<b>Kechirasiz 💎 kumushingiz yetarli emas ❌</b>")
        await asyncio.sleep(4)
        await tagmadi.delete()


@dp.callback_query_handler(text="orqa",state=Marketnig.ichiga)
async def tahxona(call:CallbackQuery):
    await call.message.answer("👩‍🌾 <b>Quyidagilardan tanlang </b>‼",reply_markup=set_ferma)
    await call.message.delete()
    await Marketnig.fermas.set()


## Quyon 5x uchun hanler 👇
## Quyon 5x uchun hanler  👇
## Quyon 5x uchun hanler   👇


@dp.callback_query_handler(text="quyon5x",state=Marketnig.fermas)
async def fermaxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    about_user = select_users(user_idn)
    about_farm = select_users_farm(user_idn)
 
    kumush = about_user[6]
    bor_quyon = about_farm[2]

    if kumush >= 69:
        gems = int(kumush) - 69
        get = int(bor_quyon) + 5
        update_farm("quyon",get,user_idn)
        update_baza("kumush",gems,user_idn)
        await call.message.answer(f"🐰 besh ta quyon sotib olindi \
            \n✅ Sizda {get} ta quyon bor",reply_markup=ichiga_kir)
        await call.message.delete()

        level_up(user_idn,30)
        await Marketnig.ichiga.set()
    else:
        tagmadi = await call.message.answer("<b>Kechirasiz 💎 kumushingiz yetarli emas ❌</b>")
        await asyncio.sleep(4)
        await tagmadi.delete()





## 1x tovuq uchun handler 👇
## 1x tovuq uchun handler  👇
## 1x tovuq uchun handler   👇


@dp.callback_query_handler(text="tovuq1x",state=Marketnig.fermas)
async def fermaxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    about_user = select_users(user_idn)
    about_farm = select_users_farm(user_idn)
 
    kumush = about_user[6]
    bor_tovuq = about_farm[3]

    if kumush >= 12:
        gems = int(kumush) - 12
        get = int(bor_tovuq) + 1
        update_farm("tovuq",get,user_idn)
        update_baza("kumush",gems,user_idn)
        await call.message.answer(f"🐓 bitta tovuq sotib olindi \
            \n✅ Sizda {get} ta tovuq bor",reply_markup=ichiga_kir)
        await call.message.delete()

        level_up(user_idn,6)
        await Marketnig.ichiga.set()
    else:
        tagmadi = await call.message.answer("<b>Kechirasiz 💎 kumushingiz yetarli emas ❌</b>")
        await asyncio.sleep(4)
        await tagmadi.delete()



## 5x tovuq uchun handler 👇
## 5x tovuq uchun handler  👇
## 5x tovuq uchun handler   👇


@dp.callback_query_handler(text="tovuq5x",state=Marketnig.fermas)
async def fermaxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    about_user = select_users(user_idn)
    about_farm = select_users_farm(user_idn)
 
    kumush = about_user[6]
    bor_tovuq = about_farm[3]

    if kumush >= 55:
        gems = int(kumush) - 55
        get = int(bor_tovuq) + 5
        update_farm("tovuq",get,user_idn)
        update_baza("kumush",gems,user_idn)
        await call.message.answer(f"🐓 beshta tovuq sotib olindi \
            \n✅ Sizda {get} ta tovuq bor",reply_markup=ichiga_kir)
        await call.message.delete()
        
        level_up(user_idn,25)
        await Marketnig.ichiga.set()
    else:
        tagmadi = await call.message.answer("<b>Kechirasiz 💎 kumushingiz yetarli emas ❌</b>")
        await asyncio.sleep(4)
        await tagmadi.delete()


### 1 ta sabzi uchun handler 👇
### 1 ta sabzi uchun handler  👇
### 1 ta sabzi uchun handler   👇

@dp.callback_query_handler(text="sabzi1",state=Marketnig.fermas)
async def Sabzixona(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    user_about = select_users(user_idn)
    farm_about = select_users_farm(user_idn)

    puli = user_about[5]
    sabzilar = farm_about[4]

    if puli >= 12:
        up_pull = int(puli) - 12
        up_sabzi = int(sabzilar) + 1
        update_baza("pul",up_pull,user_idn)
        update_farm("sabzi",up_sabzi,user_idn)
        await call.message.answer(f"🥕 1 ta sabzi sotib olindi\
            \n✅ Sizda {up_sabzi} ta sabzi bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.ichiga.set()
    else:
        balo = await call.message.answer("Sizni 💰 pulingiz yetarli emas ❌")
        await asyncio.sleep(3)
        await balo.delete()




### 10 ta sabzi uchun handler 👇
### 10 ta sabzi uchun handler  👇
### 10 ta sabzi uchun handler   👇

@dp.callback_query_handler(text="sabzi10",state=Marketnig.fermas)
async def Sabzixona(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    user_about = select_users(user_idn)
    farm_about = select_users_farm(user_idn)

    puli = user_about[5]
    sabzilar = farm_about[4]

    if puli >= 109:
        up_pull = int(puli) - 109
        up_sabzi = int(sabzilar) + 10
        update_baza("pul",up_pull,user_idn)
        update_farm("sabzi",up_sabzi,user_idn)
        await call.message.answer(f"🥕 10 ta sabzi sotib olindi\
            \n✅ Sizda {up_sabzi} ta sabzi bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.ichiga.set()
    else:
        balo = await call.message.answer("Sizni 💰 pulingiz yetarli emas ❌")
        await asyncio.sleep(3)
        await balo.delete()




### 1 ta don uchun handler 👇
### 1 ta don uchun handler  👇
### 1 ta don uchun handler   👇

@dp.callback_query_handler(text="don1",state=Marketnig.fermas)
async def Sabzixona(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    user_about = select_users(user_idn)
    farm_about = select_users_farm(user_idn)

    puli = user_about[5]
    sabzilar = farm_about[5]

    if puli >= 9:
        up_pull = int(puli) - 9
        up_sabzi = int(sabzilar) + 1
        update_baza("pul",up_pull,user_idn)
        update_farm("don",up_sabzi,user_idn)
        await call.message.answer(f"🌽 1 ta don sotib olindi\
            \n✅ Sizda {up_sabzi} ta donlar bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.ichiga.set()
    else:
        balo = await call.message.answer("Sizni 💰 pulingiz yetarli emas ❌")
        await asyncio.sleep(3)
        await balo.delete()



### 10 ta don uchun handler 👇
### 10 ta don uchun handler  👇
### 10 ta don uchun handler   👇

@dp.callback_query_handler(text="don10",state=Marketnig.fermas)
async def Sabzixona(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    user_about = select_users(user_idn)
    farm_about = select_users_farm(user_idn)

    puli = user_about[5]
    sabzilar = farm_about[5]

    if puli >= 79:
        up_pull = int(puli) - 79
        up_sabzi = int(sabzilar) + 10
        update_baza("pul",up_pull,user_idn)
        update_farm("don",up_sabzi,user_idn)
        await call.message.answer(f"🌽 10 ta don sotib olindi\
            \n✅ Sizda {up_sabzi} ta donlar bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.ichiga.set()
    else:
        balo = await call.message.answer("Sizni 💰 pulingiz yetarli emas ❌")
        await asyncio.sleep(3)
        await balo.delete()

