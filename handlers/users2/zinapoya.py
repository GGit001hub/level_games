import asyncio
from aiogram.types import Message,CallbackQuery
from states.Levels_state import LevelUp,LevelZina
from aiogram.dispatcher import FSMContext
from keyboards.inline.savdo_button import ichiga_kir
from keyboards.inline.zina_btn import zinalar
from loader import dp

from handlers.users.functions import level_up,update_baza,select_users
from handlers.users.function_farm import update_farm,select_users_farm
from .funktions import *

syupriz = ['tovuq','gems3','pul30','lvl30','pul50','gems2','sabzi5','lvl20']

@dp.message_handler(text="🪜 Zinapoya",state=LevelUp.bosh_holat)
async def zinaxona(ms:Message,state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    user = select_others(userid)['zina']
    xabar = "🪜      <b>Zinapoya o'yin</b> batafsil /help\n"
    zina = f"<b>15</b> - zina = syupriz 🎁\n<b>14</b> - zina = bang 💣\n<b>13</b> - zina = level up +10\
        \n<b>12</b> - zina = down -5 ⬇\n<b>11</b> - zina = pul 7$ 💰\n<b>10</b> - zina = bang 💣\
        \n<b>9</b> - zina = ferma 2x🌽\n<b>8</b> - zina = level up +5\n<b>7</b> - zina = game over ❌\
        \n<b>6</b> - zina = down -3 ⬇\n<b>5</b> - zina = pul 5$ 💰\n<b>4</b> - zina = game over ❌\
        \n<b>3</b> - zina = up +2 ⬆\n<b>2</b> - zina = bang 💣\n<b>1</b> - zina = pul 2$ 💰\n\
        \n<b>Siz {user} - zinapoyada siz</b> "

    await ms.answer(f"{xabar}\n{zina}",reply_markup=zinalar)
    await LevelZina.bosh_hl.set()

@dp.message_handler(commands='help',state=LevelZina.bosh_hl)
async def pomish(ms:Message):
    xabar = "<b>Zinapoya o'yini haqida</b>\n\
        \n🎁 - Oxirgi zina ichidan kutilmagan sovg'a kutadi\
        \n💣 - Bu zinaga tushsangiz ancha pasga tushib qolasiz\
        \n❌ - Shu zinaga tushsangiz o'yin tugaydi"
    await ms.answer(xabar)


@dp.callback_query_handler(text="sovga",state=LevelZina.bosh_hl)
async def sovgaxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))
    user_info = select_users(userid)
    user_sovga = int(select_others(userid)['sovga'])

    xabar = ""
    if user_sovga >= 1:
        user_gems =int(user_info['kumush'])
        user_puli = int(user_info['pul'])
        user_tovuq = int(select_users_farm(userid)['tovuq'])
        await call.message.delete()
        user_sabzi = int(select_users_farm(userid)['sabzi'])
        podark = await call.message.answer("🛒")
        await asyncio.sleep(3)
        await podark.delete()
        sovga = r.choice(syupriz)
        if sovga == 'gems3':
            xabar += "🎁 Sovg'ani ichida  3 ta 💎 kumush yashiringan edi\
                \nKumushuingiz 3 taga ko'paydi"
            update_baza('kumush', user_gems+3, userid)
        elif sovga == 'gems2':
            xabar += "🎁 Siz tanlagan sovg'a ichida\
                \n2 ta kumush 💎 yashirilgan edi"
            update_baza('kumush', user_gems+2, userid)
        elif sovga == 'pul30':
            update_baza('pul', user_puli+30,userid)
            xabar += "🎁 Sizga 30 $ 💰 pul mukofoti tushdi"
        elif sovga == 'pul50':
            update_baza('pul', user_puli+50,userid)
            xabar += "🎁 Sizga 50 $ pul tushdi\nPulingiz 50 $ ga ko'paydi"
        elif sovga == 'tovuq':
            update_farm('tovuq', user_tovuq+1,userid)
            xabar += "🎁 1 ta tovuq yutib oldingiz\nTovuqlar 1 taga ko'paydi"
        elif sovga == 'sabzi5':
            update_farm('sabzi', user_sabzi+5, userid)
            xabar += "🎁 Sovg'a ichida quyon uchun <b>5x sabzi</b> bor edi"
        elif sovga == 'lvl20':
            level_up(userid,20)
            xabar += "🎁 Sovg'a ichida <b>+20 daraja</b> bor edi\nDarajangiz ko'tarildi"
        elif sovga == 'lvl30':
            level_up(userid,30)
            xabar += "🎁 Sovg'a ichida <b>+30 daraja</b> bor edi\nDarajangiz ko'tarildi"

        update_others('sovga',user_sovga-1,userid)
        await call.message.answer(f"{xabar}\n<b>{user_sovga-1}</b> sovg'a qoldi",reply_markup=ichiga_kir)
        await LevelZina.ichi.set()
    else:
        yuq = await call.message.answer("Kechirasiz sizda bironta sovg'a yo'q ❌")
        await asyncio.sleep(3)
        await yuq.delete()
    



@dp.callback_query_handler(text='orqa',state=LevelZina.ichi)
async def ichxona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get("user_id"))

    user = select_others(userid)['zina']
    zina = f"🪜      <b>Zinapoya o'yin</b> batafsil /help\n<b>15</b> - zina = syupriz 🎁\n<b>14</b> - zina = bang 💣\n<b>13</b> - zina = level up +10\
        \n<b>12</b> - zina = down -5 ⬇\n<b>11</b> - zina = pul 7$ 💰\n<b>10</b> - zina = bang 💣)\
        \n<b>9</b> - zina = ferma 2x🌽\n<b>8</b> - zina = level up +5\n<b>7</b> - zina = game over ❌)\
        \n<b>6</b> - zina = down -3 ⬇\n<b>5</b> - zina = pul 5$ 💰\n<b>4</b> - zina = game over ❌)\
        \n<b>3</b> - zina = up +2 ⬆\n<b>2</b> - zina = bang 💣\n<b>1</b> - zina = pul 2$ 💰\n\
        \n<b>Siz {user} - zinapoyada siz</b> "
    await call.message.answer(zina,reply_markup=zinalar)
    await call.message.delete()
    await LevelZina.bosh_hl.set()