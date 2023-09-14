# ki.txt beolvasása
class Beolvas:
    def __init__(self, allomanynev):
        self.adatok = []
        with open(allomanynev, "r", encoding="UTF8") as file:
            for x in file:
                self.adatok.append(x)

#class Rendezés:




b = Beolvas("ki.txt")   