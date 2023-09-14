# ki.txt beolvasása
class Beolvas:
    def __init__(self):
        self.adatok = []
        with open("ki.txt", "r", encoding="UTF8") as file:
            for x in file:
                self.adatok.append(x.strip(";"))

class Rendezés:
    def AlphaOrInt(self, list):
        i = 0
        s = 0
        barmi_mas = 0
        for x in range(len(list)):
            if (x.isalpha()):
                s += 1
            if (x.isnumeric()):
                i += 1    
            else:
                barmi_mas = 1
        
        aOi = ""
        if (s == len(list)):
            aOi = "string"
        if (i == len(list)):
            aOi = "int"
        if (barmi_mas == 1):
            aOi = "Hiba"

        return aOi    