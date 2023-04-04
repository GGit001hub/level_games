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

import asyncio



@dp.callback_query_handler(text="orqa",state=Marketnig.kumush_ichi)
async def Orxona(call:CallbackQuery):
    await call.message.answer("💎 <b>Qancha kumush xarid qilasiz</b> ❓",reply_markup=kumush_set)
    await call.message.delete()
    await Marketnig.kumushs.set()




@dp.callback_query_handler(text="gems1",state=Marketnig.kumushs)
async def Kumxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    user_idn = int(user_idn)

    about_user = select_users(user_idn)
    dengi = int(about_user['pul'])
    kumush = int(about_user['kumush'])

    if dengi >= 59:
        updengi = int(dengi) - 59
        up_kumush = int(kumush) + 1
        update_baza("pul",updengi,user_idn)
        update_baza("kumush",up_kumush,user_idn)

        await call.message.answer(f"✅ Kumushingiz 1 taga ko'paydi\
            \n💎 Sizda {up_kumush} ta kumush bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.kumush_ichi.set()
    else:
        balo = await call.message.answer("Sizni 💰 pulingiz yetarli emas ❌")
        await asyncio.sleep(3)
        await balo.delete()



## 10 ta kumush uchun handler 👇
## 10 ta kumush uchun handler  👇
## 10 ta kumush uchun handler   👇
@dp.callback_query_handler(text="gems10",state=Marketnig.kumushs)
async def Kumxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")
    user_idn = int(user_idn)

    about_user = select_users(user_idn)
    dengi = int(about_user['pul'])
    kumush = int(about_user['kumush'])

    if dengi >= 549:
        updengi = int(dengi) - 549
        up_kumush = int(kumush) + 10
        update_baza("pul",updengi,user_idn)
        update_baza("kumush",up_kumush,user_idn)

        await call.message.answer(f"✅ Kumushingiz 10 taga ko'paydi\
            \n💎 Sizda {up_kumush} ta kumush bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.kumush_ichi.set()
    else:
        balo = await call.message.answer("Sizni 💰 pulingiz yetarli emas ❌")
        await asyncio.sleep(3)
        await balo.delete()






## 1 ta pul uchun handler 👇
## 1 ta pul uchun handler  👇
## 1 ta pul uchun handler   👇

# @dp.callback_query_handler(text="gems1",state=Marketnig.kumushs)
# async def Kumxona(call:CallbackQuery, state:FSMContext):
#     date = await state.get_data()
#     user_idn = date.get("user_id")
#     user_idn = int(user_idn)

#     about_user = select_users(user_idn)
#     dengi = about_user[5]
#     kumush = about_user[6]

#     if dengi >= 549:
#         updengi = int(dengi) - 549
#         up_kumush = int(kumush) + 10
#         update_baza("pul",updengi,user_idn)
#         update_baza("kumush",up_kumush,user_idn)

#         await call.message.answer(f"✅ Kumushingiz 10 taga ko'paydi\
#             \n💎 Sizda {up_kumush} ta kumush bor",reply_markup=ichiga_kir)

#         await call.message.delete()
#         await Marketnig.kumush_ichi.set()
#     else:
#         balo = await call.message.answer("Sizni 💰 pulingiz yetarli emas ❌")
#         await asyncio.sleep(3)
#         await balo.delete()



