from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

reklama1 = [InlineQueryResultArticle(
    id="nonenoene1",
    title="Reklama - 1",
    input_message_content=InputTextMessageContent(
        message_text="ā¼ Telegramdaga yangi bot\nš¤ @level_gamebot bu bot bilan zerikmaysiz\
            \nš® Ko'plab o'yinlari bor"
        
    ),
    reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[
                InlineKeyboardButton("1 - batlle",callback_data="asd"),
                InlineKeyboardButton("2 - batlle",callback_data="asssa")
            ]])
)
]


reklama2 = [InlineQueryResultArticle(
    id="no23renoene1",
    title="Reklama - 2",
    input_message_content=InputTextMessageContent(
        message_text="š¤ Bot: @level_gamebot\nā Ko'plab o'yinlar\nā Battle qilish"
    ),
    thumb_url="https://yandex.ru/images/search?text=phot&img_url=http%3A%2F%2Fimg4.goodfon.ru%2Foriginal%2F2560x1600%2Fb%2F39%2Fedita-vilkeviciute-model-cherno-beloe-1.jpg&pos=10&rpt=simage&stype=image&lr=10335&parent-reqid=1677426334300735-14638152938061334329-vla1-3137-980-vla-l7-balancer-8080-BAL-5990&source=serp"
)
]
