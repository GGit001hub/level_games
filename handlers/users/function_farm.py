import sqlite3
import pymongo
from pymongo import MongoClient
import random as r

cluster = MongoClient('mongodb://localhost:27017')
user = cluster['level_game']
collection_farm = user['farms']

others = cluster['level_game']
collection_others = others['others']


def create_farm(name,idn):
    """Farm yaratish uchun funksiya"""
    about = {'_id':idn, 'name':name, 'quyon':0, 'tovuq':0, 'sabzi':0, 'don':0, 'lvlquyon':'1,0/10', 'lvltovuq':'1,0/10'}
    collection_farm.insert_one(about)


def select_users_farm(idn):
    """ID raqam bo'yicah Foydalanuvchi malumootlarini qaytaruvchi funksiya"""
    farm = collection_farm.find_one({'_id':idn})
    return farm


    # db = sqlite3.connect("data/farms.db")
    # user = db.execute(F"SELECT * FROM Shopping where idn={idn}")
    # return user.fetchone()
    
# print(select_users_farm(1173831936))


def update_farm(nimani,nimaga,ids):
    son = collection_farm.update_one({'_id':int(ids)},{'$set':{f"{nimani}":f"{nimaga}"}})
    return "true"


def level_quyon(ids,lvl):
    """Quyonni darajasini ko'tarish uchun  funksiya"""
    malumot = collection_farm.find_one({'_id':ids})

    aboutlvl = malumot['lvlquyon'].split(",")
    qylvl = aboutlvl[0]
    dan = aboutlvl[-1].split("/")[-1]
    bor = aboutlvl[-1].split("/")[0]

    pilus = int(bor) + int(lvl)
    if int(pilus) >= int(dan):
        up_level = int(qylvl) + 1
        updan = int(dan) + 5
        upbor = int(pilus) - int(dan)
        yangila = f"{up_level},{upbor}/{updan}"
        collection_farm.update_one({'_id':ids},{'$set':{'lvlquyon':str(yangila)}})        
    else:
        eskila = f"{qylvl},{pilus}/{dan}"
        collection_farm.update_one({'_id':ids},{'$set':{'lvlquyon':str(eskila)}})        

    return "true"

# print(level_quyon(1173831936,3))
# print(update_farm("lvlquyon","2,0/15",1173831936))
# print(update_farm("quyon",6,1173831936))
# print(update_farm("sabzi",123,1173831936))

# text = "hello uzbekistan people"
# print("peoples" not in text)





def level_tovuq(ids,lvl):
    """Tovuqning darajasini ko'tarish uchun  funksiya"""
    malumot = collection_farm.find_one({'_id':ids})

    aboutlvl = malumot['lvltovuq'].split(",")
    qylvl = aboutlvl[0]
    dan = aboutlvl[-1].split("/")[-1]
    bor = aboutlvl[-1].split("/")[0]

    pilus = int(bor) + int(lvl)
    if int(pilus) >= int(dan):
        up_level = int(qylvl) + 1
        updan = int(dan) + 5
        upbor = int(pilus) - int(dan)
        yangila = f"{up_level},{upbor}/{updan}"
        collection_farm.update_one({'_id':ids},{'$set':{'lvltovuq':str(yangila)}})        
    else:
        eskila = f"{qylvl},{pilus}/{dan}"
        collection_farm.update_one({'_id':ids},{'$set':{'lvltovuq':str(eskila)}})        


    return "true"

# print(level_tovuq(1173831936,5))



def others_create(idn,name):
    about = {'_id':idn, 'name':name, 'profile':'None','sticker':'None','taxmin':5,'zina':0,'sovga':0}
    collection_others.insert_one(about)