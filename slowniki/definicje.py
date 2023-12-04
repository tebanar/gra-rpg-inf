def inf(dc):
    for k,v in dc.items():
        print(f"{k}  =  {v}")
def inf_all(lst:list):
    for dc in lst:
        print(40*"-")
        inf(dc)
def edycja(dc):
    print("wprowadz klucz")
    inp = input()
    dc[inp] = input("wprowadz dane ")
def wybdced(lst:list):
    inp = input("wprowadz nazwe ksiazki do edycji ")
    for dc in lst:
        if dc["nazwa"] == inp:
            edycja(dc)
def dodksiaz(lst:list):
    ileks = len(lst) + 1
    ileks = {}
    ileks["nazwa"] = input("nazwa = ")
    lst.append(ileks)
def usunksiaz(lst:list):
    inp = input("wprowadz nazwe ksiazki do usuniecia ")
    for dc in lst:
        if dc["nazwa"] == inp:
            lst.remove(dc)

    
    
