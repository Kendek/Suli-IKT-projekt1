import random
import string
db = 0
betudb = 0
i = 0
a = int(input("Írd be melyik feladatot választod(1,2,3,4):"))
lista = []
#1.feladat
if a == 1:
    with open("ki.txt", "w", encoding="utf-8") as file:
        x = int(input("Írja be a generálás mennyiségét:"))
        also = int(input("Írja be az alsó határt:"))
        felso = int(input("Írja be a felső határt:"))
        while i < x:
            szam = random.randrange(also, felso)
            i += 1
            file.write(str(szam)+ "; ")
        

#2.feladat
elif a == 2:
    with open("ki.txt", "w", encoding="utf-8") as file:
        y = int(input("Írja be a generálás mennyiségét:"))
        while db < y:
            db += 1
            for i in range(1,20):
                betu = random.choice(string.ascii_letters)
                file.write(betu)
                betudb += 1
                if betudb == 20:
                    file.write("; ")
                    betudb = 0


#3.feladat
elif a == 3:
    with open("ki.txt", "r", encoding="utf-8") as file:
        x = int(input("Írja be a generálás mennyiségét:"))
        also = int(input("Írja be az alsó határt:"))
        felso = int(input("Írja be a felső határt:"))
        lista = file.read().removesuffix(";").split(";")
        if len(lista) == x:
            helyes = True
            for szam in lista:
                if int(szam) > felso or int(szam) < also:
                    helyes = False
            if helyes:
                print("Megfelelt!")
            else:
                print("Nem megfelelt!")
        else:
            print("Nem megfelelt!")


#4.feladat
elif a == 4:
    with open("ki.txt", "r", encoding="utf-8") as file:
        x = int(input("Írja be a mennyiséget:"))
        lista = file.read().removesuffix(";").split(";")
        if len(lista) == x:
            print("Megfelelt!")
        else:
            print("Nem megfelelt!")

else:
    print("Nincs ilyen feladat!")
