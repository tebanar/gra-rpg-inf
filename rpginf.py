from random import randint
import potwory
import przedmioty
przedmioty.hajs = 0
jakipot = 0
przedmioty.punkty = 0
i = 0
uderz = 1

while i != 1:
        print("wybierz trudnosc")
        print("-"*40)
        print("A = latwy")
        print("B = sredni")
        print("C = trudny")
        print("-"*40)
        trudnosc = input().upper()
        print(40*"-")
        if trudnosc == 'A':
                print("poziom trudnosci - latwy")
                przedmioty.atak = 5
                dodmaxhp = 30
                dodmaxmp = 30
                potkihptr = 2
                potkimptr = 2
                i += 1
                przedmioty.punkty += 0
                print(40*"-")
        elif trudnosc == 'B':
                print("poziom trudnosci - sredni")
                przedmioty.atak = 1
                dodmaxhp = 15
                dodmaxmp = 15
                i += 1
                potkihptr = 1
                potkimptr = 1
                przedmioty.punkty += 10
                print(40*"-")
        elif trudnosc == 'C':
                print("poziom trudnosci - trudny")
                przedmioty.atak = -3
                dodmaxhp = 0
                dodmaxmp = 0
                i += 1
                potkihptr = 0
                potkimptr = 0
                przedmioty.punkty += 20
                print(40*"-")
        else:
                print("brak takiej opcji")
                print(40*"-")
                continue
# -------------------------------------------------------
    

i = 0
while i != 1:
       print("wybierz postac")
       print("A = wojownik")
       print("B = mag")
       print("C = zwiadowca")
       print("-"*40)
       postac = input().upper()

       print(40*"-")

       if postac == 'A':
              def atack():
                     global atak
                     return randint(15+przedmioty.atak, 20+przedmioty.atak)
              przedmioty.maxhp = 150 + dodmaxhp
              przedmioty.maxmp = 50 + dodmaxmp
              przedmioty.wiedz = 0
              potkihp = 3 + potkihptr
              potkimp = 1 + potkimptr
              i += 1
       if postac == 'B':
              def atack():
                     global atak
                     return randint(3+przedmioty.atak, 6+przedmioty.atak)
              przedmioty.maxhp = 70 + dodmaxhp
              przedmioty.maxmp = 150 + dodmaxmp
              przedmioty.wiedz = 2
              potkihp = 1 + potkihptr
              potkimp = 3 + potkimptr
              i += 1
       if postac == 'C':
              def atack():
                     global atak
                     return randint(7+przedmioty.atak, 13+przedmioty.atak)
              przedmioty.maxhp = 100 + dodmaxhp
              przedmioty.maxmp = 70 + dodmaxmp
              przedmioty.wiedz = 1
              potkihp = 2 + potkihptr
              potkimp = 2 + potkimptr
              i += 1
       else:
              print("brak takiej opcji")
              print(40*"-")
              continue
               
# -------------------------------------------------------
przedmioty.hp = przedmioty.maxhp
przedmioty.mp = przedmioty.maxmp
def dostdomagii():
    global wiedz
    global tarcza
    global magicznypocisk
    global blyskawica
    global meteor
    global potkihpcheck
    global potkimpcheck
    global punkty
    potkihpcheck = 0
    potkimpcheck = 0

    tarcza = 0
    magicznypocisk = 0
    blyskawica = 0
    meteor = 0
    if potkihp > 0:
          potkihpcheck = 1
    if potkimp > 0:
          potkimpcheck = 1
    if przedmioty.wiedz >= 1:
              tarcza = 1
              magicznypocisk = 1
    if przedmioty.wiedz >= 2:
              blyskawica = 1
    if przedmioty.wiedz >= 3:
              meteor = 1 
    if przedmioty.wiedz >= 4:
           przedmioty.punkty += 1
def meteordef():
       global mp
       if przedmioty.mp < 70:
        print("-"*40)
        print("Nie masz wystarczającej ilości many!")
        return 0
       przedmioty.mp -= 70
       return randint(100, 150)

def tarczadef():
       global mp
       global tarczahp
       if przedmioty.mp < 30:
        print("-"*40)
        print("Nie masz wystarczajacej ilości many!")
        return 0
       tarczahp = 0
       przedmioty.mp -= 30
       tarczahp += 20
       return 0

def magicznypociskdef():
       global mp
       if przedmioty.mp < 10:
        print("-"*40)
        print("Nie masz wystarczającej ilości many!")
        return 0
       przedmioty.mp -= 10
       return randint(20, 30)

def blyskawicadef():
       global mp
       if przedmioty.mp < 30:
        print("-"*40)
        print("Nie masz wystarczającej ilości many!")
        return 0
       przedmioty.mp -= 30
       return randint(60, 70)
# -------------------------------------------------------


# -------------------------------------------------------


def wybatak():
       global potkihp
       global potkimp
       global wybat
       global tarcza
       global magicznypocisk
       global blyskawica
       global meteor
       global hp
       global mp
       global tarczahp
       dostdomagii()
       print("co chcesz zrobić")
       print("A - uderz")

       if tarcza == 1:
              print("B - uzyc magicznej tarczy")
       if magicznypocisk == 1:
              print("C - uzyc magicznego pocisku")  
       if blyskawica == 1:
              print("D - uzyc blyskawicy")
       if meteor == 1:
              print("E - uzyc meteor")
       if potkihpcheck == 1:
             print("H - uzyc potki hp")
       if potkimpcheck == 1:
             print("M - uzyc potki mp")
       wybat = input().upper()
       if wybat == 'A':
              return atack()
       if wybat == 'B' and tarcza == 1:
              if przedmioty.mp < 30:
                     print("-"*40)
                     print("Nie masz wystarczajacej ilości many!")
                     return 0
              przedmioty.mp -= 30
              tarczahp = 20
              return 0
       elif wybat == 'B' and tarcza == 0:
              return 0
       if wybat == 'C' and magicznypocisk == 1:
              return magicznypociskdef()
       elif wybat == 'C' and magicznypocisk == 0:
              return 0
       if wybat == 'D' and blyskawica == 1:
              return blyskawicadef()
       elif wybat == 'D' and blyskawica == 0:
              return 0
       if wybat == 'E' and meteor == 1:
              return meteordef()
       elif wybat == 'E' and meteor == 0:
              return 0
       if wybat == 'H' and potkihp > 0:
             przedmioty.hp += 40
             if przedmioty.hp > przedmioty.maxhp:
                   przedmioty.hp = przedmioty.maxhp   
             potkihp -= 1
             return 0
       elif wybat == 'H' and potkihp == 0:
              return 0

                         
       if wybat == 'M' and potkimp > 0:
              przedmioty.mp += 70
              if przedmioty.mp > przedmioty.maxmp:
                   przedmioty.mp = przedmioty.maxmp
              potkimp -= 1
              return 0
       elif wybat == 'M' and potkimp == 0:
              return 0
      
       else:
              print("Nie wybrano akcji")
              return 0


       # -------------------------------------------------------

def walkazboss():
              global punkty
              global hp
              global hppot
              global tarczahp
              potwory.boss()
              potwory.bossatck()
              tarczahp = 0
              print(f"spotykasz bossa, ma on {potwory.hppot} hp i {potwory.atackpot} ataku")
              print(40*"-")
              tarczahp = 0
              while potwory.hppot > 0:
                    potwory.hppot -= wybatak()
                    print(40*"-")
                    if potwory.hppot < 0:
                           potwory.hppot = 0
                    if potwory.hppot > 0:
                        print(f"boss ma jeszcze {potwory.hppot} hp ")
                        print(40*"-")
                        if tarczahp > 0:
                               tarczahp -= potwory.atackpot
                               if tarczahp < 0:
                                      przedmioty.hp += tarczahp
                                      tarczahp = 0
                        elif tarczahp == 0:
                               przedmioty.hp -= potwory.atackpot
                        print(f"boss zadal {potwory.atackpot} obrazen")
                        print(40*"-")
                        if przedmioty.hp <= 0:
                                   return 0
                        if przedmioty.hp < 0:
                              przedmioty.hp = 0
                        print(f"masz jeszcze {przedmioty.hp}/{przedmioty.maxhp} hp, {tarczahp} tarczy i {przedmioty.mp}/{przedmioty.maxmp} mp")
                        print(40*"-")
                    else: 
                     przedmioty.punkty += 30 
                     print("pokonales bossa")
                     print(40*"-"), print("WYGRALES")


def walkazpot():
       global hajs
       global punkty
       global jakipot
       global hp
       global hppot
       global tarczahp
       jakipot = randint(1,4)
       if jakipot == 1:
              
              potwory.zombie()
              potwory.zombieatack()
              print(f"spotykasz zombie, ma on {potwory.hppot} hp i {potwory.atackpot} ataku")
              print(40*"-")
              tarczahp = 0
              while potwory.hppot > 0:
                    potwory.hppot -= wybatak()
                    print(40*"-")
                    if potwory.hppot < 0:
                           potwory.hppot = 0
                    if potwory.hppot > 0:
                        print(f"zombie ma jeszcze {potwory.hppot} hp ")
                        print(40*"-")
                        if tarczahp > 0:
                               tarczahp -= potwory.atackpot
                               if tarczahp < 0:
                                      przedmioty.hp += tarczahp
                                      tarczahp = 0
                        elif tarczahp == 0:
                               przedmioty.hp -= potwory.atackpot
                        print(f"zombie zadal {potwory.atackpot} obrazen")
                        print(40*"-")
                        if przedmioty.hp <= 0:
                                   return 0
                        if przedmioty.hp < 0:
                              przedmioty.hp = 0
                        print(f"masz jeszcze {przedmioty.hp}/{przedmioty.maxhp} hp, {tarczahp} tarczy i {przedmioty.mp}/{przedmioty.maxmp} mp")
                        print(40*"-")
                    else: 
                     przedmioty.punkty += 5 
                     print("pokonales zombie")
                     przedmioty.hajs += randint(25, 40)
                     print(40*"-")

       elif jakipot == 2:
              potwory.duch()
              potwory.duchatack()
              tarczahp = 0
              print(f"spotykasz ducha, ma on {potwory.hppot} hp i {potwory.atackpot} ataku")
              print(40*"-")
              while potwory.hppot > 0:
                    potwory.hppot -= wybatak()
                    print(40*"-")
                    if potwory.hppot < 0:
                           potwory.hppot = 0
                    if potwory.hppot > 0:
                        print(f"duch ma jeszcze {potwory.hppot} hp ")
                        print(40*"-")
                        if tarczahp > 0:
                               tarczahp -= potwory.atackpot
                               if tarczahp < 0:
                                      przedmioty.hp += tarczahp
                                      tarczahp = 0
                        elif tarczahp == 0:
                               przedmioty.hp -= potwory.atackpot
                        print(f"duch zadal {potwory.atackpot} obrazen")
                        print(40*"-")
                        if przedmioty.hp <= 0:
                                   return 0
                        if przedmioty.hp < 0:
                              przedmioty.hp = 0
                        print(f"masz jeszcze {przedmioty.hp}/{przedmioty.maxhp} hp, {tarczahp} tarczy i {przedmioty.mp}/{przedmioty.maxmp} mp")
                        print(40*"-")
                    else:
                           przedmioty.punkty += 5
                           print("pokonales ducha")
                           przedmioty.hajs += randint(25, 40)
                           print(40*"-")
       elif jakipot == 3:
              potwory.goblin()
              potwory.goblinatack()
              tarczahp = 0
              print(f"spotykasz goblina, ma on {potwory.hppot} hp i {potwory.atackpot} ataku")
              print(40*"-")
              while potwory.hppot > 0:
                    potwory.hppot -= wybatak()
                    print(40*"-")
                    if potwory.hppot < 0:
                           potwory.hppot = 0
                    if potwory.hppot > 0:
                        print(f"goblin ma jeszcze {potwory.hppot} hp ")
                        print(40*"-")
                        if tarczahp > 0:
                               tarczahp -= potwory.atackpot
                               if tarczahp < 0:
                                      przedmioty.hp += tarczahp
                                      tarczahp = 0
                        elif tarczahp == 0:
                               przedmioty.hp -= potwory.atackpot
                        print(f"goblin zadal {potwory.atackpot} obrazen")
                        print(40*"-")
                        if przedmioty.hp <= 0:
                                   return 0
                        if przedmioty.hp < 0:
                              przedmioty.hp = 0
                        print(f"masz jeszcze {przedmioty.hp}/{przedmioty.maxhp} hp, {tarczahp} tarczy i {przedmioty.mp}/{przedmioty.maxmp} mp")
                        print(40*"-")
                    else: 
                            przedmioty.punkty += 5
                            print("pokonales goblina")
                            przedmioty.hajs += randint(25, 40)
                            print(40*"-")
       if jakipot == 4:
              
              potwory.szlam()
              print(f"spotykasz slime, ma on {potwory.hppot} hp i {potwory.atackpot} ataku")
              print(40*"-")
              tarczahp = 0
              while potwory.hppot > 0:
                    potwory.hppot -= wybatak()
                    print(40*"-")
                    if potwory.hppot < 0:
                           potwory.hppot = 0
                    if potwory.hppot > 0:
                        print(f"slime ma jeszcze {potwory.hppot} hp ")
                        print(40*"-")
                        if tarczahp > 0:
                               tarczahp -= potwory.atackpot
                               if tarczahp < 0:
                                      przedmioty.hp += tarczahp
                                      tarczahp = 0
                        elif tarczahp == 0:
                               przedmioty.hp -= potwory.atackpot
                        print(f"slime zadal {potwory.atackpot} obrazen")
                        print(40*"-")
                        if przedmioty.hp <= 0:
                                   return 0
                        if przedmioty.hp < 0:
                              przedmioty.hp = 0
                        print(f"masz jeszcze {przedmioty.hp}/{przedmioty.maxhp} hp, {tarczahp} tarczy i {przedmioty.mp}/{przedmioty.maxmp} mp")
                        print(40*"-")
                    else: 
                     przedmioty.punkty += 5 
                     print("pokonales slime")
                     przedmioty.hajs += randint(25, 40)
                     print(40*"-")
  
# -------------------------------------------------------
def ognisko():
       global hp
       global mp
       global potkihp
       global potkimp
       print("odpoczywasz i dostajesz 50 hp, 50 mp, 1 potke hp i 1 potke mp")
       print(40*"-")
       przedmioty.hp += 50
       przedmioty.mp += 50
       if przedmioty.mp > przedmioty.maxmp:
              przedmioty.mp = przedmioty.maxmp
       if przedmioty.hp > przedmioty.maxhp:
              przedmioty.hp = przedmioty.maxhp
       potkihp += 1
       potkimp += 1

def magicznykamien():
       global atak 
       global maxhp
       global maxmp
       global mp
       global hp
       przedmioty.atak += 5
       przedmioty.maxhp += 20
       przedmioty.hp += 20
       przedmioty.maxmp += 30
       przedmioty.mp += 30


# ---------------------------------------------------------------------------------
def liczbprzedsklep():
       global lprzed
       global przed1
       global przed2
       global przed3
       lprzed = randint(1,3)
       print(f"jest {lprzed} przedmiotow do kupienia")
       print(40*"-")

       if lprzed == 1:
              przed1 = randint(1,4)
              if przed1 == 1:
                     print("jest korona wiedzy")
                     print(40*"-")
              elif przed1 == 2:
                     print("jest helm many")
                     print(40*"-")
              elif przed1 == 3:
                     print("jest miecz")
                     print(40*"-")
              elif przed1 == 4:
                      print("jest kula mocy")
                      print(40*"-")
       if lprzed == 2:
              przed1 = randint(1,4)
              if przed1 == 1:
                     print("jest korona wiedzy")
                     print(40*"-")
              elif przed1 == 2:
                     print("jest helm many")
                     print(40*"-")
              elif przed1 == 3:
                     print("jest miecz")
                     print(40*"-")
              elif przed1 == 4:
                      print("jest kula mocy")
                      print(40*"-")
              przed2 = randint(1,4)
              if przed2 == 1:
                     print("jest korona wiedzy")
                     print(40*"-")
              elif przed2 == 2:
                     print("jest helm many")
                     print(40*"-")
              elif przed2 == 3:
                     print("jest miecz")
                     print(40*"-")
              elif przed2 == 4:
                      print("jest kula mocy")
                      print(40*"-")
       elif lprzed == 3:
              przed1 = randint(1,4)
              if przed1 == 1:
                     print("jest korona wiedzy")
                     print(40*"-")
              elif przed1 == 2:
                     print("jest helm many")
                     print(40*"-")
              elif przed1 == 3:
                     print("jest miecz")
                     print(40*"-")
              elif przed1 == 4:
                      print("jest kula mocy")
                      print(40*"-")
              przed2 = randint(1,4)
              if przed2 == 1:
                     print("jest korona wiedzy")
                     print(40*"-")
              elif przed2 == 2:
                     print("jest helm many")
                     print(40*"-")
              elif przed2 == 3:
                     print("jest miecz")
                     print(40*"-")
              elif przed2 == 4:
                      print("jest kula mocy")
                      print(40*"-")
              przed3 = randint(1,4)
              if przed3 == 1:
                     print("jest korona wiedzy")
                     print(40*"-")
              elif przed3 == 2:
                     print("jest helm many")
                     print(40*"-")
              elif przed3 == 3:
                     print("jest miecz")
                     print(40*"-")
              elif przed3 == 4:
                      print("jest kula mocy")
                      print(40*"-")

def sklep():
       global punkty
       global maxmp
       global maxhp
       global dotkskarb
       global mp
       global hp
       global atak
       global wiedz
       global taka
       global lprzed
       global przed1
       global przed2
       global przed3
       global hajs
       liczbprzedsklep()
       if lprzed == 1:
                     while True:
                            print(f"masz {przedmioty.hajs} hajsu")
                            print("czy kupujesz (100 hajsu)?")
                            print(40*"-")
                            print("A - tak")
                            print("B - nie")
                            print(40*"-")
                            taka = input().upper()
                            if taka == 'A' and przed1 == 1 and przedmioty.hajs >= 100:
                                   print("kupujesz korone wiedzy")
                                   print(40*"-")
                                   przedmioty.korwiedz()
                                   przedmioty.hajs -= 100
                                   break
                            elif taka == 'A'and przed1 == 1 and przedmioty.hajs < 100:
                                   print("nie masz wystarczajaco pieniedzy")
                                   break
                                   
                            elif taka == 'A' and przed1 == 2 and przedmioty.hajs >= 100:
                                   print("kupujesz helm many")
                                   print(40*"-")
                                   przedmioty.helmman()
                                   przedmioty.hajs -= 100
                                   break
                            elif taka == 'A'and przed1 == 2 and przedmioty.hajs < 100:
                                   print("nie masz wystarczajaco pieniedzy")
                                   break


                            if taka == 'A' and przed1 == 3 and przedmioty.hajs >= 100:
                                   print("kupujesz korone wiedzy")
                                   print(40*"-")
                                   przedmioty.miecz()
                                   przedmioty.hajs -= 100
                                   break
                            elif taka == 'A'and przed1 == 3 and przedmioty.hajs < 100:
                                   print("nie masz wystarczajaco pieniedzy")
                                   break

                            elif taka == 'A' and przed1 == 4 and przedmioty.hajs >= 100:
                                   print("kupujesz kule mocy")
                                   print(40*"-")
                                   przedmioty.kulamocy()
                                   przedmioty.hajs -= 100
                                   break
                            elif taka == 'A'and przed1 == 4 and przedmioty.hajs < 100:
                                   print("nie masz wystarczajaco pieniedzy")
                                   break

                            elif taka == 'B':
                                   print("nic nie kupujesz")
                                   break
                            else:
                                   print("nic nie wybrales")
                                   continue

       elif lprzed == 2:
              while True:
                     print(f"masz {przedmioty.hajs} hajsu")
                     print("co kupujesz (100 hajsu)")
                     print(40*"-")
                     print("A - kupujesz przedmiot 1")
                     print("B - kupujesz przedmiot 2")
                     print("C - nic nie kupujesz")


                     taka = input().upper()
                     if taka == 'A' and przed1 == 1 and przedmioty.hajs >= 100:
                            print("kupujesz korone wiedzy")
                            print(40*"-")
                            przedmioty.korwiedz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 1 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'A' and przed1 == 2 and przedmioty.hajs >= 100:
                            print("kupujesz helm many")
                            print(40*"-")
                            przedmioty.helmman()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 2 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'A' and przed1 == 3 and przedmioty.hajs >= 100:
                            print("miecz")
                            print(40*"-")
                            przedmioty.miecz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 3 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     elif taka == 'A' and przed1 == 4 and przedmioty.hajs >= 100:
                            print("kupujesz kule mocy")
                            print(40*"-")
                            przedmioty.kulamocy()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 4 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'B' and przed2 == 1 and przedmioty.hajs >= 100:
                            print("kupujesz korone wiedzy")
                            print(40*"-")
                            przedmioty.korwiedz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed2 == 1 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'B' and przed2 == 2 and przedmioty.hajs >= 100:
                            print("kupujesz helm many")
                            print(40*"-")
                            przedmioty.helmman()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'B'and przed2 == 2 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'B' and przed2 == 3 and przedmioty.hajs >= 100:
                            print("miecz")
                            print(40*"-")
                            przedmioty.miecz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'B'and przed2 == 3 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     elif taka == 'B' and przed2 == 4 and przedmioty.hajs >= 100:
                            print("kupujesz kule mocy")
                            print(40*"-")
                            przedmioty.kulamocy()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'B'and przed2 == 4 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     elif taka == 'C':
                            print("nic nie kupujesz")
                            break
                     else:
                            print("nic nie wybrales")
                            continue
       elif lprzed == 3:
              print(f"masz {przedmioty.hajs} hajsu")
              print("co kupujesz (100 hajsu)")
              print(40*"-")
              print("A - kupujesz przedmiot 1")
              print("B - kupujesz przedmiot 2")
              print("C - kupujesz przedmiot 3")
              print("D - nic nie kupujesz")

              while True:


                     taka = input().upper()
                     if taka == 'A' and przed1 == 1 and przedmioty.hajs >= 100:
                            print("kupujesz korone wiedzy")
                            print(40*"-")
                            przedmioty.korwiedz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 1 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'A' and przed1 == 2 and przedmioty.hajs >= 100:
                            print("kupujesz helm many")
                            print(40*"-")
                            przedmioty.helmman()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 2 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'A' and przed1 == 3 and przedmioty.hajs >= 100:
                            print("miecz")
                            print(40*"-")
                            przedmioty.miecz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 3 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     elif taka == 'A' and przed1 == 4 and przedmioty.hajs >= 100:
                            print("kupujesz kule mocy")
                            print(40*"-")
                            przedmioty.kulamocy()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'A'and przed1 == 4 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'B' and przed2 == 1 and przedmioty.hajs >= 100:
                            print("kupujesz korone wiedzy")
                            print(40*"-")
                            przedmioty.korwiedz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'B'and przed2 == 1 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'B' and przed2 == 2 and przedmioty.hajs >= 100:
                            print("kupujesz helm many")
                            print(40*"-")
                            przedmioty.helmman()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'B'and przed2 == 2 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'B' and przed2 == 3 and przedmioty.hajs >= 100:
                            print("miecz")
                            print(40*"-")
                            przedmioty.miecz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'B'and przed2 == 3 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     elif taka == 'B' and przed2 == 4 and przedmioty.hajs >= 100:
                            print("kupujesz kule mocy")
                            print(40*"-")
                            przedmioty.kulamocy()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'B' and przed2 == 4 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'C' and przed3 == 1 and przedmioty.hajs >= 100:
                            print("kupujesz korone wiedzy")
                            print(40*"-")
                            przedmioty.korwiedz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'C'and przed3 == 1 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'C' and przed3 == 2 and przedmioty.hajs >= 100:
                            print("kupujesz helm many")
                            print(40*"-")
                            przedmioty.helmman()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'C'and przed3 == 2 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     if taka == 'C' and przed3 == 3 and przedmioty.hajs >= 100:
                            print("miecz")
                            print(40*"-")
                            przedmioty.miecz()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'C'and przed3 == 3 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     elif taka == 'C' and przed3 == 4 and przedmioty.hajs >= 100:
                            print("kupujesz kule mocy")
                            print(40*"-")
                            przedmioty.kulamocy()
                            przedmioty.hajs -= 100
                            break
                     elif taka == 'C'and przed3 == 4 and przedmioty.hajs < 100:
                            print("nie masz wystarczajaco pieniedzy")
                            break

                     elif taka == 'D':
                            print("nic nie kupujesz")
                            break
                     else:
                            print("nic nie wybrales")
                            continue
                     
              




# ---------------------------------------------------------------------------------
              
def event():
       
       global jakievent
       global hp
       global punkty
       global x
       global y
       global atak
       global maxmp
       global mp
       global maxhp
       global hp

       jakievent = randint(1,10)
       if jakievent == 1:
              print("znajdujesz skrzynkę")
              print(40*"-")
              skarbpokoj()
       elif jakievent == 2:
              print("spotykasz potwora")
              print(40*"-")
              walkazpot()
       elif jakievent == 3:
              print("znalazles ognisko")
              print(40*"-")
              przedmioty.punkty += 2
              ognisko()
       elif jakievent == 4:
              print("znalazles magiczny kamien")
              print(40*"-")
              przedmioty.punkty += 2
              magicznykamien()
       elif jakievent == 5:
              print("wszedles w pulapke")
              print(40*"-")
              przedmioty.hp -= 20
              if przedmioty.hp <= 0:
                     przedmioty.hp = 1
       elif jakievent == 6:
              print("znalazles sklep")
              print(40*"-")
              sklep()
       elif jakievent >= 7 and jakievent <= 9:
              print("znalazles obelisk")
              print(40*"-")
              x = randint(1,3)
              if x == 1:
                     print("jest to obelisk ataku")
                     print("czy chcesz go dotknac? (+ 3 ataku, -30 max many)")
                     print("A - tak")
                     print("B - nie")
                     y = input().upper()
                     if y == 'A':
                            przedmioty.atak += 3
                            przedmioty.maxmp -= 30
                            if przedmioty.mp > przedmioty.maxmp:
                                   przedmioty.mp = przedmioty.maxmp
                     elif y == 'B':
                            print("nie dotykasz obelisku")
              if x == 2:
                     print("jest to obelisk many")
                     print("czy chcesz go dotknac? (-10 max hp, +30 max many)")
                     print("A - tak")
                     print("B - nie")
                     y = input().upper()
                     if y == 'A':
                            przedmioty.maxhp -= 10
                            przedmioty.maxmp += 30
                            if przedmioty.hp > przedmioty.maxhp:
                                   przedmioty.hp = przedmioty.maxhp
                     elif y == 'B':
                            print("nie dotykasz obelisku")
              if x == 3:
                     print("jest to obelisk hp")
                     print("czy chcesz go dotknac? (+20 max hp, -1 ataku)")
                     print("A - tak")
                     print("B - nie")
                     y = input().upper()
                     if y == 'A':
                            przedmioty.maxhp += 20
                            przedmioty.atak -= 1
                     elif y == 'B':
                            print("nie dotykasz obelisku")
       elif jakievent == 10:
              print("znajdujesz przedmiot ale zeby go wziasc dostaniesz 20 obrazen")
              print("A - bierzesz")
              print("B - nic z nim nie robisz")
              y = input().upper()
              if y == 'A':
                     x = randint(1,100)
                     if x >= 1 and x <= 25:
                            print("dostajesz helm many")
                            przedmioty.helmman()
                            przedmioty.hp -= 20
                            if przedmioty.hp < 0:
                                    przedmioty.hp = 1

                     elif x >= 26 and x <= 50:
                            print("dostajesz korone wiedzy")
                            przedmioty.korwiedz()
                            przedmioty.hp -= 20
                            if przedmioty.hp < 0:
                                    przedmioty.hp = 1
                     elif x >= 51 and x <= 75:
                            print("dostajesz miecz")
                            przedmioty.miecz()
                            przedmioty.hp -= 20
                            if przedmioty.hp < 0:
                                    przedmioty.hp = 1
                     elif x >= 76 and x <= 94:
                             print("dostajesz kule mocy")
                             przedmioty.kulamocy()
                             if przedmioty.hp < 0:
                                    przedmioty.hp = 1
                     elif x >= 95 and x <= 100:
                            print("dostajesz god mode")
                            przedmioty.maxhp += 10000
                            przedmioty.hp += 10000
                            przedmioty.mp += 10000
                            przedmioty.maxmp += 10000
                            przedmioty.hp -= 20
                            przedmioty.atak += 100

              elif y == 'B':
                     print("nic nie robisz")


def skarbpokoj():
       global punkty
       global maxmp
       global maxhp
       global dotkskarb
       global szansanamimika
       global mp
       global hp
       global jakiskarb
       global atak
       global wiedz
       while True:
              print("otworzyc skrzynie?")
              print(40*"-")
              print("A - tak")
              print("B - nie")
              print(40*"-")
              dotkskarb = input().upper()
              if dotkskarb == 'A': 
                     szansanamimika = randint(1, 1000)
                     if szansanamimika == 1:
                            przedmioty.hp = 0
                            if przedmioty.hp <= 0:
                            
                                   print("to byl mimik i cie zjadl")
                                   print(40*"-")
                                   break
                     else:
                            jakiskarb = randint(1,7)
                            if jakiskarb == 1:
                                   print("dostales helmet many")
                                   print(40*"-")
                                   przedmioty.helmman()
                                   break
                            elif jakiskarb == 2:
                                   print("dostales miecz")
                                   print(40*"-")
                                   przedmioty.miecz()
                                   break
                            elif jakiskarb == 3:
                                   print("dostales korone wiedzy")
                                   print(40*"-")
                                   przedmioty.korwiedz()
                                   break
                            elif jakiskarb == 4:
                                   print("nic nie bylo w skrzyni")
                                   print(40*"-")
                                   break
                            elif jakiskarb == 5:
                                   print("dostales kule mocy")
                                   print(40*"-")
                                   przedmioty.kulamocy()
                                   break
                            elif jakiskarb == 6:
                                   print("znalazles troche pieniedzy")
                                   przedmioty.hajsskrzynia()
                                   break
                            else:
                                   print("w skrzyni byla pulapka")
                                   print(40*"-")
                                   przedmioty.hp -= 10
                                   if przedmioty.hp <= 0:
                                          przedmioty.hp = 1
                                   break
              elif dotkskarb == 'B':
                     print("nie dotykasz skrzyni")
                     print(40*"-")
                     break
              else:
                     print("nie ma takiej opcji")
                     print(40*"-")
                     continue

# -------------------------------------------------------


def lijakpok():
       global lpok
       global jakipokoj1
       global jakipokoj2
       global jakipokoj3
       global dzrwi
       dzrwi = randint(1,10)
       if dzrwi == 1:
              lpok = 1
       elif dzrwi >= 2 and dzrwi <= 5:
              lpok = 2
       elif dzrwi > 5:
              lpok = 3
              
       print(f"jest {lpok} drzwi")
       print(40*"-")

       if lpok == 1:
              jakipokoj1 = randint(1,10)
              if jakipokoj1 == 1 or jakipokoj1 == 2:
                     print("sa drzwi z znakiem zapytania")
                     print(40*"-")
              elif jakipokoj1 == 3 or jakipokoj1 == 4:
                     print("sa drzwi z znakiem skarbu")
                     print(40*"-")
              elif jakipokoj1 >= 5 and jakipokoj1 <= 9:
                     print("sa drzwi z czaska")
                     print(40*"-")
              elif jakipokoj1 == 10:
                     print("sa drzwi z znakiem monety")
                     print(40*"-")
       elif lpok == 2:
              jakipokoj1 = randint(1,10)
              if jakipokoj1 == 1 or jakipokoj1 == 2:
                     print("sa drzwi z znakiem zapytania")
                     print(40*"-")
              elif jakipokoj1 == 3 or jakipokoj1 == 4:
                     print("sa drzwi z znakiem skarbu")
                     print(40*"-")
              elif jakipokoj1 >= 5 and jakipokoj1 <= 9:
                     print("sa drzwi z czaska")
                     print(40*"-")
              elif jakipokoj1 == 10:
                     print("sa drzwi z znakiem monety")
                     print(40*"-")
              jakipokoj2 = randint(1,10)
              if jakipokoj2 == 1 or jakipokoj2 == 2:
                     print("sa drzwi z znakiem zapytania")
                     print(40*"-")
              elif jakipokoj2 == 3 or jakipokoj2 == 4:
                     print("sa drzwi z znakiem skarbu")
                     print(40*"-")
              elif jakipokoj2 >= 5 and jakipokoj2 <= 9:
                     print("sa drzwi z czaska")
                     print(40*"-")
              elif jakipokoj2 == 10:
                     print("sa drzwi z znakiem monety")
                     print(40*"-")
       elif lpok == 3:
              jakipokoj1 = randint(1,10)
              if jakipokoj1 == 1 or jakipokoj1 == 2:
                     print("sa drzwi z znakiem zapytania")
                     print(40*"-")
              elif jakipokoj1 == 3 or jakipokoj1 == 4:
                     print("sa drzwi z znakiem skarbu")
                     print(40*"-")
              elif jakipokoj1 >= 5 and jakipokoj1 <= 9:
                     print("sa drzwi z czaska")
                     print(40*"-")
              elif jakipokoj1 == 10:
                     print("sa drzwi z znakiem monety")
                     print(40*"-")
              jakipokoj2 = randint(1,10)
              if jakipokoj2 == 1 or jakipokoj2 == 2:
                     print("sa drzwi z znakiem zapytania")
                     print(40*"-")
              elif jakipokoj2 == 3 or jakipokoj2 == 4:
                     print("sa drzwi z znakiem skarbu")
                     print(40*"-")
              elif jakipokoj2 >= 5 and jakipokoj2 <= 9:
                     print("sa drzwi z czaska")
                     print(40*"-")
              elif jakipokoj2 == 10:
                     print("sa drzwi z znakiem monety")
                     print(40*"-")
              jakipokoj3 = randint(1,10)
              if jakipokoj3 == 1 or jakipokoj3 == 2:
                     print("sa drzwi z znakiem zapytania")
                     print(40*"-")
              elif jakipokoj3 == 3 or jakipokoj3 == 4:
                     print("sa drzwi z znakiem skarbu")
                     print(40*"-")
              elif jakipokoj3 >= 5 and jakipokoj3 <= 9:
                     print("sa drzwi z czaska")
                     print(40*"-")
              elif jakipokoj3 == 10:
                     print("sa drzwi z znakiem monety")
                     print(40*"-")

              
# -------------------------------------------------------

def ilepokijakpok():
       global jakipokoj1
       global i
       global maxhp
       global maxmp
       global hp
       global mp

       global taka
       global czypotworodp
       global potkihp
       global potkimp



       lijakpok()
       while True:
              if lpok == 1:
                     print("czy wchodzisz do nich?")
                     print(40*"-")
                     print("A - tak")
                     print("B - nie")
                     print(40*"-")
                     taka = input().upper()
                     if taka == 'A' and jakipokoj1 >= 1 and jakipokoj1 <= 2:
                            print("wchodzisz do dzrwi z znakiem zapytania")
                            print(40*"-")
                            event()
                            break
                     elif taka == 'A' and jakipokoj1 >= 3 and jakipokoj1 <= 4:
                            print("wchodzisz do pokoju z znakiem skarbu")
                            print(40*"-")
                            skarbpokoj()
                            break
                     elif taka == 'A' and jakipokoj1 >= 5 and jakipokoj1 <= 9:
                            print("wchodisz do pokoju z czaszka")
                            print(40*"-")
                            walkazpot()
                            break
                     elif taka == 'A' and jakipokoj1 == 10 :
                            print("wchodisz do sklepu")
                            print(40*"-")
                            sklep()
                            break

                     elif taka == 'B':
                            print("co robisz")
                            print(40*"-")
                            print("A - idziesz dalej")
                            print("B - odpoczywasz (20 procent szansy na atak potwora)")
                            if potkihp > 0:
                                   print("H - pijesz potke hp")
                            if potkimp > 0:
                                   print("M - pijesz potke mp")
                            taka = input().upper()
                            if taka == 'A' and jakipokoj1 >= 1 and jakipokoj1 <= 2:
                                   print("wchodzisz do dzrwi z znakiem zapytania")
                                   print(40*"-")
                                   event()
                                   break
                            elif taka == 'A' and jakipokoj1 >= 3 and jakipokoj1 <= 4:
                                   print("wchodzisz do pokoju z znakiem skarbu")
                                   print(40*"-")
                                   skarbpokoj()
                                   break
                            elif taka == 'A' and jakipokoj1 >= 5 and jakipokoj1 <= 9:
                                   print("wchodisz do pokoju z czaszka")
                                   print(40*"-")
                                   walkazpot()
                                   break
                            elif taka == 'A' and jakipokoj1 == 10 :
                                   print("wchodisz do sklepu")
                                   print(40*"-")
                                   sklep()
                                   break
                            elif taka == 'B':
                                   print("odpoczywasz (+10 hp, +10 mp)")
                                   print(40*"-")
                                   przedmioty.hp += 10
                                   przedmioty.mp += 10
                                   if przedmioty.hp > przedmioty.maxhp:
                                          przedmioty.hp = przedmioty.maxhp
                                   if przedmioty.mp > przedmioty.maxmp:
                                          przedmioty.mp = przedmioty.maxmp
                                   czypotworodp = randint(1,5)
                                   if czypotworodp == 1:
                                          walkazpot()
                                          if przedmioty.hp <= 0:
                                                 break
                                   continue


                                   


                            elif taka == 'H' and potkihp > 0:
                                   przedmioty.hp += 40
                                   if przedmioty.hp > przedmioty.maxhp:
                                          przedmioty.hp = przedmioty.maxhp
                                   potkihp -= 1
                                   continue
                            

                            elif taka == 'M' and potkimp >0:
                                   przedmioty.mp += 70
                                   if przedmioty.mp > przedmioty.maxmp:
                                          przedmioty.mp = przedmioty.maxmp
                                   potkimp -= 1
                                   continue








              elif lpok == 2:
                     print("co robisz")
                     print(40*"-")
                     print("A - wchodzisz do 1 drzwi")
                     print("B - wchodzisz do 2 drzwi")
                     print("C - odpoczywasz (20 procent szansy na atak potwora)")
                     if potkihp > 0:
                                   print("H - pijesz potke hp")
                     if potkimp > 0:
                            print("M - pijesz potke mp")

                     taka = input().upper()
                     if taka == 'A' and jakipokoj1 >= 1 and jakipokoj1 <= 2:
                                   print("wchodzisz do dzrwi z znakiem zapytania")
                                   print(40*"-")
                                   event()
                                   break
                     elif taka == 'A' and jakipokoj1 >= 3 and jakipokoj1 <= 4:
                                   print("wchodzisz do pokoju z znakiem skarbu")
                                   print(40*"-")
                                   skarbpokoj()
                                   break
                     elif taka == 'A' and jakipokoj1 >= 5 and jakipokoj1 <= 9:
                                   print("wchodisz do pokoju z czaszka")
                                   print(40*"-")
                                   walkazpot()
                                   break
                     elif taka == 'A' and jakipokoj1 == 10 :
                                   print("wchodisz do sklepu")
                                   print(40*"-")
                                   sklep()
                                   break
                     if taka == 'B' and jakipokoj2 >= 1 and jakipokoj2 <= 2:
                                   print("wchodzisz do dzrwi z znakiem zapytania")
                                   print(40*"-")
                                   event()
                                   break
                     elif taka == 'B' and jakipokoj2 >= 3 and jakipokoj2 <= 4:
                                   print("wchodzisz do pokoju z znakiem skarbu")
                                   print(40*"-")
                                   skarbpokoj()
                                   break
                     elif taka == 'B' and jakipokoj2 >= 5 and jakipokoj2 <= 9:
                                   print("wchodisz do pokoju z czaszka")
                                   print(40*"-")
                                   walkazpot()
                                   break
                     elif taka == 'B' and jakipokoj2 == 10 :
                                   print("wchodisz do sklepu")
                                   print(40*"-")
                                   sklep()
                                   break
                     if taka == 'C':
                                   print("odpoczywasz (+10 hp, +10 mp)")
                                   print(40*"-")
                                   przedmioty.hp += 10
                                   przedmioty.mp += 10
                                   if przedmioty.hp > przedmioty.maxhp:
                                          przedmioty.hp = przedmioty.maxhp
                                   if przedmioty.mp > przedmioty.maxmp:
                                          przedmioty.mp = przedmioty.maxmp
                                   czypotworodp = randint(1,5)
                                   if czypotworodp == 1:
                                          walkazpot()
                                          if przedmioty.hp <= 0:
                                                 break


                                   continue

                     elif taka == 'H' and potkihp > 0:
                                   przedmioty.hp += 40
                                   if przedmioty.hp > przedmioty.maxhp:
                                          przedmioty.hp = przedmioty.maxhp
                                   potkihp -= 1
                                   continue
                            
                     elif taka == 'M' and potkimp > 0:
                                   przedmioty.mp += 70
                                   if przedmioty.mp > przedmioty.maxmp:
                                          przedmioty.mp = przedmioty.maxmp
                                   potkimp -= 1
                                   continue
                                   
              elif lpok == 3:
                            print("co robisz?")
                            print(40*"-")
                            print("A - wchodzisz do 1 drzwi")
                            print("B - wchodzisz do 2 drzwi")
                            print("C - wchodzisz do 3 drzwi")
                            print("D - odpoczywasz (20 procent szansy na atak potwora)")
                            if potkihp > 0:
                                   print("H - pijesz potke hp")
                            if potkimp > 0:
                                   print("M - pijesz potke mp")
                            taka = input().upper()
                            if taka == 'A' and jakipokoj1 >= 1 and jakipokoj1 <= 2:
                                                 print("wchodzisz do dzrwi z znakiem zapytania")
                                                 print(40*"-")
                                                 event()
                                                 break
                            elif taka == 'A' and jakipokoj1 >= 3 and jakipokoj1 <= 4:
                                                 print("wchodzisz do pokoju z znakiem skarbu")
                                                 print(40*"-")
                                                 skarbpokoj()
                                                 break
                            elif taka == 'A' and jakipokoj1 >= 5 and jakipokoj1 <= 9:
                                                 print("wchodisz do pokoju z czaszka")
                                                 print(40*"-")
                                                 walkazpot()
                                                 break
                            elif taka == 'A' and jakipokoj1 == 10 :
                                                 print("wchodisz do sklepu")
                                                 print(40*"-")
                                                 sklep()
                                                 break
                            elif taka == 'B' and jakipokoj2 >= 1 and jakipokoj2 <= 2:
                                                 print("wchodzisz do dzrwi z znakiem zapytania")
                                                 print(40*"-")
                                                 event()
                                                 break
                            elif taka == 'B' and jakipokoj2 >= 3 and jakipokoj2 <= 4:
                                                 print("wchodzisz do pokoju z znakiem skarbu")
                                                 print(40*"-")
                                                 skarbpokoj()
                                                 break
                            elif taka == 'B' and jakipokoj2 >= 5 and jakipokoj2 <= 9:
                                                 print("wchodisz do pokoju z czaszka")
                                                 print(40*"-")
                                                 walkazpot()
                                                 break
                            elif taka == 'B' and jakipokoj2 == 10 :
                                                 print("wchodisz do sklepu")
                                                 print(40*"-")
                                                 sklep()
                                                 break
                            elif taka == 'C' and jakipokoj3 >= 1 and jakipokoj3 <= 2:
                                                 print("wchodzisz do dzrwi z znakiem zapytania")
                                                 print(40*"-")
                                                 event()
                                                 break
                            elif taka == 'C' and jakipokoj3 >= 3 and jakipokoj3 <= 4:
                                                 print("wchodzisz do pokoju z znakiem skarbu")
                                                 print(40*"-")
                                                 skarbpokoj()
                                                 break
                            elif taka == 'C' and jakipokoj3 >= 5 and jakipokoj3 <= 9:
                                                 print("wchodisz do pokoju z czaszka")
                                                 print(40*"-")
                                                 walkazpot()
                                                 break
                            elif taka == 'C' and jakipokoj3 == 10 :
                                                 print("wchodisz do sklepu")
                                                 print(40*"-")
                                                 sklep()
                                                 break
                            
                            elif taka == 'D':
                                          print("odpoczywasz (+10 hp, +10 mp)")
                                          print(40*"-")
                                          przedmioty.hp += 10
                                          przedmioty.mp += 10
                                          if przedmioty.hp > przedmioty.maxhp:
                                                 przedmioty.hp = przedmioty.maxhp
                                          if przedmioty.mp > przedmioty.maxmp:
                                                 przedmioty.mp = przedmioty.maxmp
                                          czypotworodp = randint(1,5)
                                          if czypotworodp == 1:
                                                 walkazpot()
                                                 if przedmioty.hp <= 0:
                                                         break


                                          continue
                                          


                            elif taka == 'H' and potkihp > 0:
                                          przedmioty.hp += 40
                                          if przedmioty.hp > przedmioty.maxhp:
                                                 przedmioty.hp = przedmioty.maxhp
                                          potkihp -= 1
                                          continue
                                          

                            elif taka == 'M' and potkimp > 0:
                                          przedmioty.mp += 70
                                          if przedmioty.mp > przedmioty.maxmp:
                                                 przedmioty.mp = przedmioty.maxmp
                                          potkimp -= 1
                                          continue
                                          
# -------------------------------------------------------
for i in range(30):
    ilepokijakpok()
    if przedmioty.hp <= 0:
      break
if przedmioty.hp > 0:
       walkazboss()
       print("-"*40)
       print(f"PUNKTY - {przedmioty.punkty} ")
       print("-"*40)
if przedmioty.hp <= 0:
      print("game over")
      print(f"PUNKTY - {przedmioty.punkty} ")
      print("-"*40)