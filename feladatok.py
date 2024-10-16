import random

def feladat_1():
    szam:int = int(input("Adj megy egy páratlan számot: "))
    while(szam%2==0):
        print("Páros")
        szam:int = int(input("Páratlan számot adj meg! "))
    print("Páratlan a szám!")

def feladat_2():
    ottel_osztahto:int = 0
    for i in range(0,7,1):
        i:int = int(random.random()*96)+5
        print(i)
        if(i%5==0):
            ottel_osztahto += 1 
        i += 1
    print(f"A számok között {ottel_osztahto} db 5-el osztahtó szám van")

def feladat_3(text,betu):
    db:int = 0
    print("A szöveg hossza: ", len(text))
    for i in range(0, len(text), 1):
        if(text[i]==betu):
            db += 1
    print(f"A szövegben {db} '{betu}' betű van.")


def feladat_4():
    nev:str = str(input("Adj meg egy nevet: ('@'-t a kilépéshez) "))
    tarolas = [] 
    while(nev=="@"):
        tarolas.append(nev)
        nev:str = str(input("Adj meg egy nevet: ('@'-t a kilépéshez) "))
        print("Ennyi nevet adott meg: ",)


