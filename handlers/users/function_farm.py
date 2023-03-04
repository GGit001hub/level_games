import sqlite3



def create_farm(name,idn):
    db = sqlite3.connect("data/farms.db")
    db.execute(f"""INSERT INTO Shopping VALUES ("{name}",'{idn}','0','0','0','0',"1,0/10","1,0/10")""")
    db.commit()


def select_users_farm(idn):
    """ID raqam bo'yicah Foydalanuvchi malumootlarini qaytaruvchi funksiya"""
    db = sqlite3.connect("data/farms.db")
    user = db.execute(F"SELECT * FROM Shopping where idn={idn}")
    return user.fetchone()

# print(select_users_farm(1173831936))


def update_farm(nimani,nimaga,ids):
    db = sqlite3.connect("data/farms.db")
    barcha = db.execute(f"UPDATE Shopping SET {nimani}='{nimaga}' WHERE idn={ids}")
    db.commit()
    return "true"


def level_quyon(ids,lvl):
    """Quyonni darajasini ko'tarish uchun  funksiya"""
    db = sqlite3.connect("data/farms.db")
    user = db.execute(F"SELECT * FROM Shopping where idn={ids}")
    malumot = user.fetchone()

    aboutlvl = malumot[6].split(",")
    qylvl = aboutlvl[0]
    dan = aboutlvl[-1].split("/")[-1]
    bor = aboutlvl[-1].split("/")[0]

    pilus = int(bor) + int(lvl)
    if int(pilus) >= int(dan):
        up_level = int(qylvl) + 1
        updan = int(dan) + 5
        upbor = int(pilus) - int(dan)
        yangila = f"{up_level},{upbor}/{updan}"
        db.execute(f"UPDATE Shopping SET lvlquyon=\"{yangila}\" WHERE idn={ids}")
    else:
        eskila = f"{qylvl},{pilus}/{dan}"
        db.execute(f"UPDATE Shopping SET lvlquyon=\"{eskila}\" WHERE idn={ids}")

    db.commit()
    return "true"

# print(level_quyon(1173831936,15))
# print(update_farm("lvlquyon","2,0/15",1173831936))
# print(update_farm("quyon",6,1173831936))
# print(update_farm("sabzi",123,1173831936))

# text = "hello uzbekistan people"
# print("peoples" not in text)





def level_tovuq(ids,lvl):
    """Tovuqning darajasini ko'tarish uchun  funksiya"""
    db = sqlite3.connect("data/farms.db")
    user = db.execute(F"SELECT * FROM Shopping where idn={ids}")
    malumot = user.fetchone()

    aboutlvl = malumot[7].split(",")
    qylvl = aboutlvl[0]
    dan = aboutlvl[-1].split("/")[-1]
    bor = aboutlvl[-1].split("/")[0]

    pilus = int(bor) + int(lvl)
    if int(pilus) >= int(dan):
        up_level = int(qylvl) + 1
        updan = int(dan) + 5
        upbor = int(pilus) - int(dan)
        yangila = f"{up_level},{upbor}/{updan}"
        db.execute(f"UPDATE Shopping SET lvltovuq=\"{yangila}\" WHERE idn={ids}")
    else:
        eskila = f"{qylvl},{pilus}/{dan}"
        db.execute(f"UPDATE Shopping SET lvltovuq=\"{eskila}\" WHERE idn={ids}")

    db.commit()
    return "true"

# print(level_tovuq(1099273252,2))



def death_func():
    pass