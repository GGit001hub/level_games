from aiogram.types import Message, CallbackQuery
from loader import dp,bot
from .functions import *

from states.All_State import *
from states.Levels_state import *
from keyboards.default.for_start import *
from keyboards.inline.farm_inline import *

import random as r


frm = sqlite3.connect("data/farms.db")
creat_frm = frm.execute("""CREATE TABLE IF NOT EXISTS Shopping (name TEXT,idn INT,quyon INT,tovuq INT,sabzi INT,don INT,lvlquyon TEXT,lvltovuq TEXT)""")


@dp.message_handler(text="Boshqalar...",state=Games.bosh_holat)
async def Boshqalar(ms:Message):
    await ms.answer("Ferma bo'limi 👩‍🌾",reply_markup=ruyxat_inline)
    await Farms.bosh_holat.set()



@dp.callback_query_handler(text="orqaga",state=Farms.bosh_holat)
async def Orqag(call:CallbackQuery):
    await call.message.answer("Bosh sahifa",reply_markup=level_games)
    await call.message.delete()
    await Games.bosh_holat.set() 