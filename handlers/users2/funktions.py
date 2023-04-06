import random as r
from .words import lugat
from .words1 import dicttion
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://baza:github_2005@cluster1.laecs6u.mongodb.net/?retryWrites=true&w=majority")

others = cluster['level_game']
collection_others = others['others']


def get_words():
    dikt = r.choice(lugat)
    while "-" in dikt or ' ' in dikt:
        dikt = r.choice(lugat)
    return dikt.upper()

def set_words():
    dic = r.choice(dicttion)
    return dic.lower()


def display(foydalanuvchi, lugat):
    d_l = ''
    for harf in lugat:
        if harf in foydalanuvchi.upper():
            d_l += harf
        else:
            d_l += '_'
    return d_l



def select_others(ids):
    finsa = collection_others.find_one({'_id':ids})
    return finsa


def update_others(nimani, nimaga, ids):
    """Bazaga o'zgartirish kiritish uchun yasalgan funksiya"""
    son = collection_others.update_one({'_id':ids},{'$set':{f"{nimani}":f"{nimaga}"}})
    return "true"
    