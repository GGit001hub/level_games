from aiogram.types import Message,CallbackQuery
from loader import dp,bot
from aiogram.dispatcher import FSMContext

from states.All_State import *
from handlers.users.functions import select_users,update_baza
from keyboards.default.for_start import *
from keyboards.default.uyinlar import *
from keyboards.inline.pul_uvhun import *
from .funktions import select_others,set_words
import asyncio
import random as r

ch_tir = []
yutuq = []
xato_javob = []


@dp.message_handler(text="🔀 Chalkash harflar",state=PulTop.turlar)
async def Turkalar(ms:Message, state:FSMContext):
    date =await state.get_data()
    userid = int(date.get("user_id"))
    taxmin = int(select_others(userid)['taxmin'])
    xato_javob.clear()
    for tx in range(taxmin):
        xato_javob.append(1)
    malumot = f"O'yini to'xtatish uchun <b><code>stop</code></b> so'zini kiriting \
        \n1 ta to'g'ri javob = 2 $, \nBatafsil /about ustiga bosing"
    yutuq.clear()
    await ms.answer(malumot,reply_markup=boshla)
    await ms.delete()   
    await Chalkash.aralash.set()


@dp.message_handler(commands='about',state=Chalkash.aralash)
async def aboutxona(ms:Message):
    xabar = "<b>So'z chalkashtrish o'yini</b>\n\
        \nBu o'yinda bot sizga <b>inglis tilidagi</b> so'zni o'rinlarini almashtirib beradi\
        \nSiz jo'yini to'g'rilab kiritasiz"
    await ms.answer(xabar)

@dp.callback_query_handler(text='boshlash',state=Chalkash.aralash)
async def boshlaxona(call:CallbackQuery,state:FSMContext):
    taxminiy_soz = set_words()
    print(taxminiy_soz)
    await state.update_data(togri = taxminiy_soz)
    ## chalkashtirihs funksiyasi
    for ts in taxminiy_soz:
        ch_tir.append(ts)
    r.shuffle(ch_tir)## yangi funksiya
    chalkash = ''
    for tg in ch_tir:
        chalkash += tg
    await call.message.answer(f"👍 Men bitta so'z chalkashtirdim 😄\
        \n🤔 Topishga harakat qiling 🫵 : <b>{chalkash}</b>")
    ch_tir.clear()
    await call.message.delete()
    await Chalkash.taxmin.set()


@dp.message_handler(state=Chalkash.taxmin)
async def chtirxona(ms:Message, state:FSMContext):
    date = await state.get_data()
    togri_soz = date.get("togri")
    userid = int(date.get('user_id'))
    taxmin = ms.text.lower()
    if xato_javob:
        if taxmin != 'stop':
            if taxmin == togri_soz:
                balo = await ms.answer(f"✅<b> To'g'ri topdingiz</b>\n<b>{togri_soz} so'zi edi</b>")
                taxminiy_soz = set_words()
                yutuq.append(2)
                await state.update_data(togri = taxminiy_soz)
                ## chalkashtirihs funksiyasi
                for ts in taxminiy_soz:
                    ch_tir.append(ts)
                r.shuffle(ch_tir)## yangi funksiya
                chalkash = ''
                for tg in ch_tir:
                    chalkash += tg
                await ms.answer(f"👍 Men yana bitta so'z chalkashtirdim 😄\
                    \n🤔 Topishga harakat qiling 🫵 : <b>{chalkash}</b>")
                ch_tir.clear()
                await Chalkash.taxmin.set()
                await asyncio.sleep(5)
                await balo.delete()
            else:
                xato_javob.remove(1)
                nalo = await ms.answer(f"✖ <b>Noto'g'ri javob kiritildi</b>\nXato javoblar: {len(xato_javob)}")
                await asyncio.sleep(4)
                await nalo.delete()
        else:
            pul = int(select_users(userid)['pul'])
            update_baza('pul',pul+sum(yutuq),userid)
            await ms.answer(f"Yutib olgan pulingiz: <b>{sum(yutuq)} $</b> bo'ldi",reply_markup=pul_tanlash)
            yutuq.clear()
            await PulTop.turlar.set()

    else:
        pul = int(select_users(userid)['pul'])
        print(yutuq)
        update_baza('pul',pul+sum(yutuq),userid)
        await ms.answer(f"Imkoniyatingiz tugadi ❗\nYutib olgan pulingiz: <b>{sum(yutuq)} $</b> bo'ldi",reply_markup=pul_tanlash)
        yutuq.clear()
        await PulTop.turlar.set()
    # if 





