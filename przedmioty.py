hajs = 0
atak = 0
wiedz = 0
punkty = 0
maxmp = 0
mp = 0
hp = 0
maxhp = 0
atak = 0
def korwiedz():
       global wiedz 
       global punkty
       global maxmp
       global mp
       wiedz += 1
       maxmp += 30
       mp += 30
       punkty += 5
       return wiedz, maxmp, mp, punkty
def miecz():
       global atak
       global punkty
       atak  += 5
       punkty += 2
       return atak, punkty
def helmman():
       global hp
       global mp
       global maxhp
       global maxmp
       global punkty
       maxhp += 30
       maxmp += 100
       hp += 30
       mp += 100
       punkty += 4
       return maxhp, maxmp, hp, mp, punkty

def kulamocy():
       global hp
       global mp
       global maxhp
       global maxmp
       global atak
       global punkty
       maxhp += 30
       maxmp += 30
       hp += 30
       mp += 30
       atak += 3
       punkty += 5
       return maxhp, maxmp, hp, mp, atak, punkty

def hajsskrzynia():
       global hajs
       global punkty
       hajs += 200
       punkty += 1
       return hajs, punkty
