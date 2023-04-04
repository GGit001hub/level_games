import asyncio
from aiogram.types import CallbackQuery
from states.Levels_state import LevelUp,LevelZina
from aiogram.dispatcher import FSMContext
from keyboards.default.uyinlar import level_up_button
from keyboards.inline.zina_btn import zinalar
from loader import dp

from handlers.users.functions import level_up,update_baza,select_users
from handlers.users.function_farm import update_farm,select_users_farm
from .funktions import *
import random as r

syupriz = ['tovuq','gems3','pul30','pul50','gems2','sabzi5']


@dp.callback_query_handler(text="orqaga",state=LevelZina.bosh_hl)
async def orqaxona(call:CallbackQuery):
    await call.message.answer("Quyidagilardan tanlang 👇",reply_markup=level_up_button)
    await call.message.delete()
    await LevelUp.bosh_holat.set()

@dp.callback_query_handler(text="aylantir",state=LevelZina.bosh_hl)
async def aylanxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    info = select_others(userid) 
    turgan_zina = int(info['zina'])
    user_puli = int(select_users(userid)['pul'])
    user_doni = int(select_users_farm(userid)['don'])
    # user_gems = int(select_users(userid)['kumush'])
    # user_tovuq = int(select_users_farm(userid)['tovuq'])
    # user_sabzi = int(select_users_farm(userid)['sabzi'])
    xabar = ""
    if user_puli >= 12:
        update_baza('pul',user_puli-12,userid)
        await call.message.delete()
        omad = r.randint(1,4)
        update_zina = turgan_zina + omad
        vabo = await call.message.answer(f"Sizga <b>{omad}</b> raqami tushdi ✅")
        await asyncio.sleep(3)
        await vabo.delete()
        if update_zina == 1:
            update_baza('pul', user_puli+2, userid)
            update_others('zina', 1, userid)
            xabar += "Siz 2 $ pul yutdingiz"
        elif update_zina == 2:
            update_others('zina', 1, userid)
            xabar += "Sizga \"BANG\" tushdi"
        elif update_zina == 3:
            update_others('zina', 5, userid)
            xabar += "Siz 2 zina yuqoriga ko'tarildingiz"
        elif update_zina == 4:
            update_others('zina', 0, userid)
            xabar += "4 - zinada siga \"❌\" tushdi. O'yin tugadi"
        elif update_zina == 5:
            update_baza('pul', user_puli+5, userid)
            update_others('zina', 5, userid)
            xabar += "Siz 5 $ yutib oldingiz"
        elif update_zina == 6:
            update_others('zina', 3, userid)
            xabar += "6- zinadan 3 zina pastga tushdingiz"
        elif update_zina == 7:
            update_others('zina', 0, userid)
            xabar += "7- zinada siga \"❌\" tushdi. O'yin tugadi"
        elif update_zina == 8:
            update_others('zina', 8, userid)
            level_up(userid, 5)
            xabar += "Darajangiz ko'tarildi +5"
        elif update_zina == 9:
            update_others('zina', 9, userid)
            update_farm('don', user_doni+2, userid)
            xabar += "Tovuq uchun 2x don qo'shildi"
        elif update_zina == 10:
            update_others('zina', 3, userid)
            xabar += "10- zinada sizga \"BANG\" tushdi. Siz 3-zinada siz"
        elif update_zina == 11:
            update_others('zina', 11, userid)
            update_baza('pul', user_puli+7, userid)
            xabar += "Pulingiz 7$ ko'paydi"
        elif update_zina == 12:
            update_others('zina', 7 ,userid)
            xabar += "12- zinadan siz 7- zinaga sakradingiz"
        elif update_zina == 13:
            update_others('zina', 13, userid)
            level_up(userid, 10)
            xabar += "Darjangiz +10 ga ko'tarildi"
        elif update_zina == 14:
            update_others('zina', 5, userid)
            xabar += "14- zinada Sizga \"BANG\" tushdi. Siz 5-zinada"
        elif update_zina >= 15:
            suvga = int(select_others(userid))['sovga']
            update_others('sovga',suvga+1,userid)
            xabar += "✨ Siz o'yinda g'olib bo'ldingiz 🎉\
                \n🎁 Va 1 ta sovg'aga ega bo'ldingiz. Sovg'ani ochishingiz mumkin ✅"
            update_others('zina', 0, userid)
        
        user = select_others(userid)['zina']
        zina = f"🪜      <b>Zinapoya o'yin</b> batafsil /help\n<b>15</b> - zina = syupriz 🎁\n<b>14</b> - zina = bang 💣\n<b>13</b> - zina = level up +10\
            \n<b>12</b> - zina = down -5 ⬇\n<b>11</b> - zina = pul 7$ 💰\n<b>10</b> - zina = bang 💣)\
            \n<b>9</b> - zina = ferma 2x🌽\n<b>8</b> - zina = level up +5\n<b>7</b> - zina = game over ❌)\
            \n<b>6</b> - zina = down -3 ⬇\n<b>5</b> - zina = pul 5$ 💰\n<b>4</b> - zina = game over ❌)\
            \n<b>3</b> - zina = up +2 ⬆\n<b>2</b> - zina = bang 💣\n<b>1</b> - zina = pul 2$ 💰\n\
            \n<b>Siz {user} - zinapoyada siz</b> "

        await call.message.answer(f"\n{zina}\n{xabar}",reply_markup=zinalar)
    else:
        balo = await call.message.answer("Sizni pulingiz yetarli emas !")
        await asyncio.sleep(3)
        await balo.delete()
