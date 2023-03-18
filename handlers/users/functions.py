import sqlite3


def register_account(idn,name,phone,pasword):
    """Yangi foydalanvhini ro'yxatdan o'tkizadi"""
    db = sqlite3.connect("data/malumotlar.db")
    db.execute(f"""INSERT INTO Users VALUES ('{idn}',"{name}",'{phone}',"{pasword}","1,0/10",'0','0','0',"quizsz")""")
    db.commit()


def select_users(idn):
    """ID raqam bo'yicah Foydalanuvchi malumootlarini qaytaruvchi funksiya"""
    db = sqlite3.connect("data/malumotlar.db")
    user = db.execute(F"SELECT * FROM Users where idn={idn}")
    return user.fetchone()

print(select_users(1173831936))
# print(select_users(1173831936)[4].split(",")[0])
# s = a.split(",")
# print(s[0])


def tekshirish(id):
    """Bazada bo yoki yo'qligini teksiruvchi funksiya"""
    db = sqlite3.connect("data/malumotlar.db")
    barcha = db.execute("SELECT * FROM Users")
    retri = ['false']
    for cdn in barcha:
        if cdn[0] == id:
            retri.append('true')
    return(retri[-1])



def pullari(idn):
    """ID raqam bo'yicha userning pulini ko'rsatadi"""
    db = sqlite3.connect("data/malumotlar.db")
    barcha = db.execute(f"SELECT * FROM Users where idn={idn}")
    hisob = barcha.fetchone()
    return hisob[5]
# print(pullari(1173831936))


def update_baza(nimani,nimaga,id):
    """Bazaga o'zgartirish kiritish uchun yasalgan funksiya"""
    db = sqlite3.connect("data/malumotlar.db")
    barcha = db.execute(f"UPDATE Users SET {nimani}='{nimaga}' WHERE idn={id}")
    db.commit()
    return "true"

# update_baza('pul',1000,1173831936)
# update_baza('kumush',500,1173831936)



def user_name(name):
    """Account nomi bo'yicha tekshiradi"""
    db = sqlite3.connect("data/malumotlar.db")
    barcha = db.execute(f"SELECT * FROM Users where name=\"{name}\"")
    hisob = barcha.fetchone()
    if hisob:
        return f"{hisob[1]},{hisob[3]},{hisob[0]}"
    else:
        return "None1None2"
# print(user_name(name="😱 Jake"))


## darajani ko'tarish uchun funksiya 👇
def level_up(ids,lvl):
    """Foydalanuvchini darajasini ko'taruvchi funksiya"""
    db = sqlite3.connect("data/malumotlar.db")
    user = db.execute(F"SELECT * FROM Users where idn={ids}")
    malumot = user.fetchone()

    daraja = malumot[4]
    ajratish = daraja.split(",")
    level = ajratish[0]
 
    mini_lugat = ajratish[-1].split("/")
    # print(mini_lugat)
    dan = mini_lugat[-1]
    uzi_bor = mini_lugat[0]
    # print(uzi_bor,1001)
    qushildi = int(uzi_bor) + lvl
    
    if int(qushildi) >= int(dan):
        update_levl = int(level) + 1
        update_dan = int(dan) + 5
        update_bor = int(qushildi) - int(dan)
        yangilash = f"{update_levl},{update_bor}/{update_dan}"
        # print(yangilash)
        barcha = db.execute(f"UPDATE Users SET level='{yangilash}' WHERE idn={ids}")
    else:
        eskilash = f"{level},{qushildi}/{dan}"
        # print(eskilash)
        barcha = db.execute(f"UPDATE Users SET level='{eskilash}' WHERE idn={ids}")
    db.commit()
    return "true"





def name_get(name):
    """Bazada bo yoki yo'qligini teksiruvchi funksiya"""
    db = sqlite3.connect("data/malumotlar.db")
    barcha = db.execute("SELECT * FROM Users")
    retri = ['false']
    for cdn in barcha:
        if cdn[1] == name:
            retri.append('true')
    return(retri[-1]) 
