from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.All_State import *
from states.Levels_state import *



@dp.message_handler(CommandHelp(),state=Quizs.all_states_names)
@dp.message_handler(CommandHelp(),state=PulTop.all_states_names)
@dp.message_handler(CommandHelp(),state=Farms.all_states_names)
@dp.message_handler(CommandHelp(),state=LevelUp.all_states_names)
@dp.message_handler(CommandHelp(),state=Games.all_states_names)
async def bot_help(message: types.Message):
    text = "Buyruqlar:\
            \n/start - Botni ishga tushirish\
            \n/help - Yordam\
            \n/profile - Account haqida malumot"
    await message.answer(text)
    

@dp.message_handler(CommandHelp(),state=Register.all_states_names)
@dp.message_handler(CommandHelp(),state=Games.all_states_names)
@dp.message_handler(CommandHelp(),state=Nastroyka.all_states_names)
async def Helpxona(ms:types.Message):
    text = "Buyruqlar:\
            \n/start - Botni ishga tushirish\
            \n/help - Yordam\
            \n/profile - Account haqida malumot\
            \n📃 <b>Parolingiz yoki acount nomingiz esdan chiqgan bo'lsa adminga murojat qiling</b>\
            \n<b>Admin</b>: <a href='https://t.me/Bot_creatorN1'>https://t.me/Bot_creatorN1</a>"
    await ms.answer(text)