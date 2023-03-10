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
    await call.message.answer("š <b>Qancha kumush xarid qilasiz</b> ā",reply_markup=kumush_set)
    await call.message.delete()
    await Marketnig.kumushs.set()




@dp.callback_query_handler(text="gems1",state=Marketnig.kumushs)
async def Kumxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")

    about_user = select_users(user_idn)
    dengi = about_user[5]
    kumush = about_user[6]

    if dengi >= 59:
        updengi = int(dengi) - 59
        up_kumush = int(kumush) + 1
        update_baza("pul",updengi,user_idn)
        update_baza("kumush",up_kumush,user_idn)

        await call.message.answer(f"ā Kumushingiz 1 taga ko'paydi\
            \nš Sizda {up_kumush} ta kumush bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.kumush_ichi.set()
    else:
        balo = await call.message.answer("Sizni š° pulingiz yetarli emas ā")
        await asyncio.sleep(3)
        await balo.delete()



## 10 ta kumush uchun handler š
## 10 ta kumush uchun handler  š
## 10 ta kumush uchun handler   š
@dp.callback_query_handler(text="gems10",state=Marketnig.kumushs)
async def Kumxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    user_idn = date.get("user_id")

    about_user = select_users(user_idn)
    dengi = about_user[5]
    kumush = about_user[6]

    if dengi >= 549:
        updengi = int(dengi) - 549
        up_kumush = int(kumush) + 10
        update_baza("pul",updengi,user_idn)
        update_baza("kumush",up_kumush,user_idn)

        await call.message.answer(f"ā Kumushingiz 10 taga ko'paydi\
            \nš Sizda {up_kumush} ta kumush bor",reply_markup=ichiga_kir)

        await call.message.delete()
        await Marketnig.kumush_ichi.set()
    else:
        balo = await call.message.answer("Sizni š° pulingiz yetarli emas ā")
        await asyncio.sleep(3)
        await balo.delete()






## 1 ta pul uchun handler š
## 1 ta pul uchun handler  š
## 1 ta pul uchun handler   š

# @dp.callback_query_handler(text="gems1",state=Marketnig.kumushs)
# async def Kumxona(call:CallbackQuery, state:FSMContext):
#     date = await state.get_data()
#     user_idn = date.get("user_id")

#     about_user = select_users(user_idn)
#     dengi = about_user[5]
#     kumush = about_user[6]

#     if dengi >= 549:
#         updengi = int(dengi) - 549
#         up_kumush = int(kumush) + 10
#         update_baza("pul",updengi,user_idn)
#         update_baza("kumush",up_kumush,user_idn)

#         await call.message.answer(f"ā Kumushingiz 10 taga ko'paydi\
#             \nš Sizda {up_kumush} ta kumush bor",reply_markup=ichiga_kir)

#         await call.message.delete()
#         await Marketnig.kumush_ichi.set()
#     else:
#         balo = await call.message.answer("Sizni š° pulingiz yetarli emas ā")
#         await asyncio.sleep(3)
#         await balo.delete()



