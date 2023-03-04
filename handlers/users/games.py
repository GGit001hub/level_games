from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from .functions import *
from states.All_State import *
from states.Levels_state import *
from keyboards.default.uyinlar import *
from keyboards.default.for_start import *
from keyboards.inline.sozlamalar import *



@dp.message_handler(commands="profile",state=Games.all_states_names)
async def ProcFile(ms:Message,state:FSMContext):
    get_data = await state.get_data()
    idns = get_data.get("user_id")
    data = select_users(idns)

    ismi = data[1]
    uroven = data[4].split(",")
    lvl = uroven[0]
    pul = data[5]
    kum = data[6]
    xabar = f"👤 {ismi}\n🏆 <b>Daraja</b>: {lvl} lv\n💰 Hisobingiz: {pul} $\n💎 Kumushlar: {kum}"
    await ms.answer(xabar,reply_markup=level_games)


@dp.message_handler(commands="profile",state=Register.all_states_names)
async def Yuq(ms:Message):
    await ms.answer("Sizda hali account mavjut emas ❌")



@dp.message_handler(commands="profile",state=PulTop.all_states_names)
@dp.message_handler(commands="profile",state=Savdo5x.all_states_names)
@dp.message_handler(commands="profile",state=Savdo.all_states_names)
@dp.message_handler(commands="profile",state=Marketnig.all_states_names)
@dp.message_handler(commands="profile",state=Farms.all_states_names)
@dp.message_handler(commands="profile",state=Nastroyka.all_states_names)
@dp.message_handler(commands="profile",state=Quizs.all_states_names)
async def ProcFile(ms:Message,state:FSMContext):
    get_data = await state.get_data()
    idn = get_data.get("user_id")
    
    data = select_users(idn)
    ismi = data[1]
    uroven = data[4].split(",")
    lvl = uroven[0]
    pul = data[5]
    kum = data[6]
    xabar = f"👤 {ismi}\n🏆 Daraja: {lvl} lv\n💰 Hisobingiz: {pul} $\n💎 Kumushlar: {kum}"
    await ms.answer(xabar)




@dp.message_handler(text="🔙 Orqaga qaytish",state=PulTop.all_states_names)
async def Orqasga(ms:Message):
    xabar = "Bosh sahifa"
    await ms.answer(xabar,reply_markup=level_games)
    await ms.delete()
    await Games.bosh_holat.set()


@dp.callback_query_handler(text="black",state=Quizs.boshi)
async def BlaCk(call:CallbackQuery):
    await call.message.answer("Pul topish uchun quyidagi o'yinlar bor",reply_markup=pul_tanlash)
    await call.message.delete()
    await PulTop.turlar.set()
