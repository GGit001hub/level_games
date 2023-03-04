from aiogram.types import Message, CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext

from states.All_State import *
from states.Levels_state import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.level_inline import *


@dp.message_handler(text="Darajani ko'tarish",state=Games.bosh_holat)
async def UrvenElup(ms:Message, state:FSMContext):
    await ms.answer("Quyidagilardan tanlang 👇",reply_markup=level_up_button)
    await LevelUp.bosh_holat.set()



@dp.message_handler(text="🎲 Tosh tashlash",state=LevelUp.bosh_holat)
async def TosjSashla(ms:Message):
    xabar = "<b>3 ta birxil son tushsa yutasiz</b>\n<b>1 marta tashlash: 3 $ </b>"
    await ms.answer(xabar,reply_markup=tosh_inline)
    await LevelUp.tosh.set()






## 🔙 Shu yerdan pasti orqaga qaytish uchun yasalgan handler 🔙
## 🔙 Shu yerdan pasti orqaga qaytish uchun yasalgan handler 🔙
## 🔙 Shu yerdan pasti orqaga qaytish uchun yasalgan handler 🔙

@dp.callback_query_handler(text="orqaga",state=LevelUp.tosh)
async def Nafasm(call:CallbackQuery):
    await call.message.answer("Quyidagilardan tanlang 👇",reply_markup=level_up_button)
    await call.message.delete()
    await LevelUp.bosh_holat.set()

@dp.message_handler(text="🔙 Orqaga qaytish",state=LevelUp.bosh_holat)
async def Saksm(ms:Message):
    await ms.answer("Asosiy menyu",reply_markup=level_games)
    await Games.bosh_holat.set()

