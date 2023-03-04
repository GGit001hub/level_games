from aiogram.types import Message,CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext

from states.All_State import *
from .functions import *
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.pul_uvhun import *
import asyncio

@dp.message_handler(text="Pul topish",state=Games.bosh_holat)
async def DengiYes(ms:Message, state:FSMContext):
    await ms.answer("Pul topish uchun quyidagi o'yinlar bor",reply_markup=pul_tanlash)
    await PulTop.turlar.set()


## Omadli o'yinlar bosilsa 👇
## Omadli o'yinlar bosilsa  👇
@dp.message_handler(text="Omadli o'yinlar",state=PulTop.turlar)
async def Turkalar(ms:Message, state:FSMContext):
    await ms.answer("Qancha pul tikasiz",reply_markup=tikish)
    await ms.delete()
    await PulTop.tikish.set()


## orqaga qytish

@dp.callback_query_handler(text="back",state=PulTop.tikish)
async def Nazad(call:CallbackQuery):
    await call.message.answer("Pul topish uchun quyidagi o'yinlar bor",reply_markup=pul_tanlash)
    await PulTop.turlar.set()
    await call.message.delete()



## hisobni yuborish

@dp.callback_query_handler(text="hisobnoma",state=PulTop.tikish)
async def Nazda(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    info = date.get("user_id")

    hisob=pullari(info)
    lola = await call.message.answer(f"<b>Hisobingi: {hisob}</b> $")
    await asyncio.sleep(5)
    await lola.delete()


@dp.callback_query_handler(text="besh",state=PulTop.tikish)
async def TikTik(call:CallbackQuery,state:FSMContext):
    date=await state.get_data()
    idisi = date.get("user_id")
    puli = pullari(idisi)
    if puli >= 5:
        await call.message.answer("Qaysi raqamni tanlaysiz 👇\
            \n<b>1 $ dan 10 $ gacha pul yashiringan</b>",reply_markup=omadni_sinash)
        await PulTop.besh_tikish.set()
        await call.message.delete()
    else:
        gola = await call.message.answer("Kechirasiz sizni pulingiz yetarli emas")
        await asyncio.sleep(3)
        await gola.delete()




@dp.callback_query_handler(text="ong",state=PulTop.tikish)
async def TdikTqik(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idisi = date.get("user_id")
    puli = pullari(idisi)
    if puli >= 10:
        await call.message.answer("Qaysi raqamni tanlaysiz 👇\
            \n<b>1 $ dan 16 $ gacha pul yashiringan</b>",reply_markup=omadni_sinash)
        await PulTop.on_tikish.set()
        await call.message.delete()
    else:
        gola = await call.message.answer("Kechirasiz sizni pulingiz yetarli emas")
        await asyncio.sleep(3)
        await gola.delete()



@dp.callback_query_handler(text="onbesh",state=PulTop.tikish)
async def TikTik(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idisi = date.get("user_id")

    puli = pullari(idisi)
    if puli >= 15:
        await call.message.answer("Qaysi raqamni tanlaysiz 👇\
            \n<b>1 $ dan 25 $ gacha pul yashiringan</b>",reply_markup=omadni_sinash)
        await PulTop.onbesh_tikish.set()
        await call.message.delete()
    else:
        gola = await call.message.answer("Kechirasiz sizni pulingiz yetarli emas")
        await asyncio.sleep(3)
        await gola.delete()



@dp.callback_query_handler(text="yigirma",state=PulTop.tikish)
async def TikTik(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idisi = date.get("user_id")

    puli = pullari(idisi)
    if puli >= 20:

        await call.message.answer("Qaysi raqamni tanlaysiz 👇\
            \n<b>1 $ dan 40 $ gacha pul yashiringan</b>",reply_markup=omadni_sinash)
        await PulTop.yigirma_tikish.set()
        await call.message.delete()
    else:
        goal = await call.message.answer("Kechirasiz sizni pulingiz yetarli emas")
        await asyncio.sleep(3)
        await goal.delete()




@dp.callback_query_handler(text="ellik",state=PulTop.tikish)
async def TikTik(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    idisi = date.get("user_id")
    puli = pullari(idisi)
    if puli >= 50:
        await call.message.answer("Qaysi raqamni tanlaysiz 👇\
            \n<b>1 $ dan 70 $ gacha pul yashiringan</b>",reply_markup=omadni_sinash)
        await PulTop.ellik_tikish.set()
        await call.message.delete()
    else:
        goal = await call.message.answer("Kechirasiz sizni pulingiz yetarli emas")
        await asyncio.sleep(3)
        await goal.delete()