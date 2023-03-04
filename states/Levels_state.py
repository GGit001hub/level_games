from aiogram.dispatcher.filters.state import State, StatesGroup


class LevelUp(StatesGroup):
    bosh_holat = State()
    tosh = State()
    battle = State()
    qidirish = State()
    birga_bir = State()
    start1vs1 = State()
    id_kirit = State()

    join_zkv = State()
    get_kutish = State()
    set_kutish = State()
    id_olish = State()
    javoblar = State()
    get_javob = State()
    zakovat = State()


class Farms(StatesGroup):
    bosh_holat = State()
    quyon = State()
    tovuq = State()

    ovqat_tugadi = State()
    ovqat_tgd = State()


class Savdo(StatesGroup): ## quyon uchun savdo
    lvl1 = State()
    lvl2 = State()
    lvl3 = State()
    lvl4 = State()
    lvl5 = State()

class Savdo5x(StatesGroup): ## 5 ta quyon uchun state
    lvl1 = State()
    lvl2 = State()
    lvl3 = State()
    lvl4 = State()
    lvl5 = State()

class TVsavdo(StatesGroup): ## tovuq uchun satate
    lvl1 = State()
    lvl2 = State()
    lvl3 = State()
    lvl4 = State()
    lvl5 = State()


class TVsavdo5x(StatesGroup): ## 5 ta tovuq uchun state
    lvl1 = State()
    lvl2 = State()
    lvl3 = State()
    lvl4 = State()
    lvl5 = State()

    

class Marketnig(StatesGroup): ## Xarid qilish uchun state
    bosh_holat = State()
    kumushs = State()
    pulls = State()
    fermas = State()
    
    ichiga = State()
    kumush_ichi = State()
