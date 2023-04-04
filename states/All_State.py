from aiogram.dispatcher.filters.state import StatesGroup, State

class Register(StatesGroup):
    bosh_holat = State()
    ism = State()
    phone = State()
    age = State()
    password = State()

    login_name = State()
    login_password = State()

class Games(StatesGroup):
    bosh_holat = State()


class PulTop(StatesGroup):
    turlar = State()
    tikish = State()

    besh_tikish = State()
    on_tikish = State()
    onbesh_tikish = State()
    yigirma_tikish = State()
    ellik_tikish = State()

    reklama = State()

class Quizs(StatesGroup):
    boshi = State()
    uchtalik = State()
    beshtalik = State()
    sakistalik = State()
    ontalik = State()


class Nastroyka(StatesGroup):
    tanlash = State()
    name_set = State()
    eski_parol = State()
    password_set = State()
    phone_set = State()
    logout = State()


class Chalkash(StatesGroup):
    aralash = State()
    taxmin = State()
