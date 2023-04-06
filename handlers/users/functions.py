import sqlite3
import pymongo
from pymongo import MongoClient
import random as r

cluster = MongoClient("mongodb+srv://baza:github_2005@cluster1.laecs6u.mongodb.net/?retryWrites=true&w=majority")
user = cluster['level_game']
collection_user = user['user']


stick = ['🌟','⚡️','⚔️','❤️','🦁','🐕','🐓','🐈']


def register_account(idn,name,phone,password):
    """Yangi foydalanvhini ro'yxatdan o'tkizadi"""
    about = {'_id':idn, 'level':'1,0/10', 'name':name, 'pul':0, 'kumush': 0, 'battle':0, 'savol':'quizs', 'password':password, 'phone':phone}
    collection_user.insert_one(about)



def select_users(uid):
    """ID raqam bo'yicah Foydalanuvchi malumootlarini qaytaruvchi funksiya"""
    bemw = collection_user.find_one({'_id':uid})
    if bemw:
        return bemw


# print(select_users(1173831936))
# print(select_users(1173831936)[4].split(",")[0])
# s = a.split(",")
# print(s[0])



def tekshirish(id):
    """Bazada bor yoki yo'qligini teksiruvchi funksiya"""
    result = collection_user.find_one({'_id':id})
    if result:
        return 'true'
    else:
        return 'false'


def pullari(idn):
    """ID raqam bo'yicha userning pulini ko'rsatadi"""
    about = collection_user.find_one({'_id':idn})
    if about:
        return int(about['pul'])
# print(pullari(1173831936),type(pullari(1173831936)))


def update_baza(nimani,nimaga,id):
    """Bazaga o'zgartirish kiritish uchun yasalgan funksiya"""
    son = collection_user.update_one({'_id':id},{'$set':{f"{nimani}":f"{nimaga}"}})
    return "true"

# print(update_baza('name','ilhom',1173831936))
# update_baza('pul',1234,1173831936)
# update_baza('kumush',123,1173831936)



def user_name(name):
    """Account nomi bo'yicha tekshiradi"""
    hisob = collection_user.find_one({'name':name})
    if hisob:
        return f"{hisob['name']},{hisob['password']},{hisob['_id']}"
    else:
        return "None1None2"
# print(user_name(name="jakes"))


## darajani ko'tarish uchun funksiya 👇
def level_up(ids,lvl):
    """Foydalanuvchini darajasini ko'taruvchi funksiya"""
    malumot = collection_user.find_one({'_id':ids})

    daraja = malumot['level']
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
        collection_user.update_one({'_id':ids},{'$set':{'level':str(yangilash)}})        
    else:
        eskilash = f"{level},{qushildi}/{dan}"
        collection_user.update_one({'_id':ids},{'$set':{'level':str(eskilash)}})
    return "true"

# print(level_up(1173831936,5))



def name_get(name):
    """Bazada bor yoki yo'qligini teksiruvchi funksiya"""
    about = collection_user.find_one({'name':name})
    return about



def name_check(name):
    about = collection_user.find_one({"name":name})
    if len(name) <= 12:
        if about:
            return False
        else:
            for nm in name:
                if nm in stick:
                    return False
            return True    
    else:
        return False


def password_check(password):
    """Parol yaratishda tekshiradi"""
    sonlar = ['1','2','3','4','5','6',"7",'8','9']
    if len(password) >= 8:
        for pas in password:
            if pas in sonlar:
                return True
        return False
    else:
        return False

# print(password_check('asd6da '))