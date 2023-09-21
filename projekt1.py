import random
import string
db = 0
betudb = 0
a = int(input("Írd be melyik feladatot választod(1,2,3,4):"))
#1.feladat
if a == 1:
    x = int(input("Írja be a generálás mennyiségét:"))
    also = int(input("Írja be az alsó határt:"))
    felso = int(input("Írja be a felső határt:"))
    print("A generált számok a megadott határok között", end=":")
    while i < x:
        szam = random.randrange(also, felso)
        i += 1
        print(szam, end="; ")
        

#2.feladat
elif a == 2:
    y = int(input("Írja be a generálás mennyiségét:"))
    while db < y:
        db += 1
        for i in range(1,20):
            betu = random.choice(string.ascii_letters)
            print(betu, end="")
            betudb += 1
            if betudb == 20:
                print(end="; ")
                betudb = 0
        
