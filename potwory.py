from random import randint

def boss():
       global hppot
       hppot = randint(200, 250)
       return hppot
def bossatck():
       global atackpot
       atackpot = randint(20, 25)
       return atackpot

def szlam():
       global atackpot
       global hppot
       atackpot = randint(10, 15)
       hppot = randint(70, 90)
       return atackpot, hppot



def zombie():
       global hppot
       hppot = randint(90, 110)
       return hppot
def zombieatack():
       global atackpot
       atackpot = randint(4, 8)
       return atackpot

def duch():
       global hppot
       hppot = randint(40, 50)
       return hppot
def duchatack():
       global atackpot
       atackpot = randint(13, 17)
       return atackpot
def goblin():
       global atackpot
       global hppot
       atackpot = randint(5, 10)
       hppot = randint(55, 75)
       return atackpot and hppot
def goblinatack():
       global atackpot
       atackpot = randint(5, 10)
       return atackpot 