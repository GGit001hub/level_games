from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from .functions import select_users
from states.All_State import *
from states.Levels_state import *
from keyboards.default.uyinlar import *
from keyboards.default.for_start import level_games
from keyboards.inline.sozlamalar import *
from handlers.users2.funktions import select_others



@dp.message_handler(commands="profile",state=Games.bosh_holat)
async def ProfilAbout(ms:Message, state:FSMContext):
    data = await state.get_data()
    ids = data.get('user_id')
    
    user = select_users(uid=int(ids))
    stick = select_others(int(ids))['sticker']
    ismi = user['name']
    uroven = user['level'].split(",")
    lvl = uroven[0]
    pul = user['pul']
    kum = user['kumush']
    if stick != 'None':
         xabar = f".     {stick} {ismi} {stick}\n🏆 <b>Daraja</b>: {lvl} lv\n💰 Hisobingiz: {pul} $\n💎 Kumushlar: {kum}"
    else:
        xabar = f"👤 {ismi}\n🏆 <b>Daraja</b>: {lvl} lv\n💰 Hisobingiz: {pul} $\n💎 Kumushlar: {kum}"
    await ms.answer(xabar,reply_markup=level_games)


@dp.message_handler(commands="profile",state=LevelHarftop.all_states_names)
@dp.message_handler(commands="profile",state=LevelUp.all_states_names)
@dp.message_handler(commands="profile",state=Farms.all_states_names)
@dp.message_handler(commands="profile",state=Savdo.all_states_names)
@dp.message_handler(commands="profile",state=Marketnig.all_states_names)
@dp.message_handler(commands="profile",state=Quizs.all_states_names)
@dp.message_handler(commands="profile",state=Chalkash.all_states_names)
@dp.message_handler(commands="profile",state=PulTop.all_states_names)
async def ProfilAbout(ms:Message, state:FSMContext):
    data = await state.get_data()
    ids = data.get('user_id')
    
    user = select_users(uid=int(ids))
    stick = select_others(int(ids))['sticker']
    ismi = user['name']
    uroven = user['level'].split(",")
    lvl = uroven[0]
    pul = user['pul']
    kum = user['kumush']
    if stick != 'None':
         xabar = f".     {stick} {ismi} {stick}\n🏆 <b>Daraja</b>: {lvl} lv\n💰 Hisobingiz: {pul} $\n💎 Kumushlar: {kum}"
    else:
        xabar = f"👤 {ismi}\n🏆 <b>Daraja</b>: {lvl} lv\n💰 Hisobingiz: {pul} $\n💎 Kumushlar: {kum}"
    await ms.answer(xabar)


#         xabar = f"\n\
# 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟\n\
# 🌟      {stick} {ismi} {stick}    🌟 \n\
# 🌟  🏆 <b>Daraja</b>: {lvl} lv    🌟 \n\
# 🌟  💰 Hisobingiz: {pul} $ 🌟     🌟 \n\
# 🌟  💎 Kumushlar: {kum}           🌟 \n\
# 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 \n\
#             "






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
