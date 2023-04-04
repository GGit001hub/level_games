from aiogram.types import Message
from states.Levels_state import LevelUp,LevelHarftop
from aiogram.dispatcher import FSMContext
from keyboards.default.uyinlar import level_up_button
from loader import dp

from handlers.users.functions import level_up
from .funktions import *

kiritilgan = []
asdasd = []
topilgan = []
sozlar = []

user_taxmini = [1]


@dp.message_handler(text="🔎 Harf topish",state=LevelUp.bosh_holat)
async def eco(ms:Message, state:FSMContext):
    kiritilgan.clear()
    asdasd.clear()
    topilgan.clear()
    sozlar.clear()
    user_taxmini.clear()
    oyladim = get_words()

    date = await state.get_data()
    userid = int(date.get('user_id'))
    move = int(select_others(userid)['taxmin'])
    for mv in range(move):
        user_taxmini.append(1)
    await state.update_data(tasodifiy_harf = oyladim)
    for hrf in oyladim:
        sozlar.append(hrf)
    print(oyladim)

    xabar = f"Men {len(oyladim)} xonali so'z o'yladim\
        \nTopishga harakat qiling"
    await ms.answer(xabar)
    await LevelHarftop.taxmin.set()


@dp.message_handler(state=LevelHarftop.taxmin)
async def topxona(ms:Message, state:FSMContext):
    harakat = ms.text.upper()
    date = await state.get_data()
    harf = date.get('tasodifiy_harf')
    userid = int(date.get("user_id"))
    if user_taxmini:
        if len(harakat) == 1:# user 1 ta harf kiritsa ishlaydi xolos
            kiritilgan.append(harakat)
            foydalanuvchi = ''
            for f in kiritilgan:
                foydalanuvchi += f

            if harakat in asdasd:
                await ms.answer(f"👁‍🗨 <b>Kechirasiz bu harni oldin kiritgansiz</b>\
                    \nKiritgan harflaringiz : {foydalanuvchi}\nTaxminingiz {len(user_taxmini)} ta qoldi")
            elif harakat in sozlar:
                topilgan.append(harakat)
                
                if display(foydalanuvchi,sozlar) == harf:
                    level_up(userid,8)
                    await ms.answer(f"🎉 Tabriklayman <b>{harf}</b> so'zini to'g'ri topdingiz 🎉 va darajangiz lo'tarildi\n\
                        \n🎲 <b>Urinishlar soni</b> : {len(kiritilgan)} ta\n\
                        \n🛠 <b>Kiritilgan harflar</b> : {foydalanuvchi}",reply_markup=level_up_button)
                    sozlar.clear()
                    kiritilgan.clear()
                    asdasd.clear()
                    topilgan.clear()
                    user_taxmini.clear()
                    await LevelUp.bosh_holat.set()
                else:
                    await ms.answer(f"✅ {harakat} harfi tog'ri kiritildi\
                        \nTopilgan harflar : <b>{display(foydalanuvchi,sozlar)}</b>\
                        \nTaxminingiz {len(user_taxmini)} ta qoldi")
            
            else:
                await ms.answer(f"😔 Men o'ylagan so'z ichida <b>{harakat}</b> harfi yo'q  \
                    \n🙂 Boshqa harf kiriting : <b>{display(foydalanuvchi,sozlar)}</b>\
                    \nTaxminingiz {len(user_taxmini)} ta qoldi")

            asdasd.append(harakat)
        else:
            await ms.answer("❌ Kechirasiz Faqat 1 ta harf kiritish mumkin xolos 😔")
        try:
            user_taxmini.remove(1)
        except ValueError:
            pass
    else:
        await ms.answer(f"Sizni taxminlaringiz tugadi 😔")
        await ms.answer("Darajani ko'tarish uchun quyidagi o'yinlar bor",reply_markup=level_up_button)
        await LevelUp.bosh_holat.set()



