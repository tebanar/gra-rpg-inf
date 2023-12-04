import definicje  
ksiazka1 = {
    "nazwa" : "jak ukrasc ksiezyc",
    "cena": 30, 
    "id" : 123423443 }
ksiazka2 = {
    "nazwa" : "beton",
    "cena": 35, 
    "id" : 12342134743 }
ksiazka3 = {
    "nazwa" : "KYS",
    "cena": 20, 
    "id" : 12342676543 }
lista = [ksiazka1, ksiazka2, ksiazka3]

while True:
    definicje.inf_all(lista)
    inp = input("a - edycja ksiazki, b - dodanie ksiazki, c - usun ksazki")
    if inp == "a":
        definicje.wybdced(lista)
    elif inp == "b":
        definicje.dodksiaz(lista)
    elif inp == "c":
        definicje.usunksiaz(lista)
