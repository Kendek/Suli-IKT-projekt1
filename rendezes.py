class Rendezés:
    def __init__(self):  #Beolvassuk a ki.txt
        self.adatok = []
        with open("ki.txt", "r", encoding="UTF8") as file:
            for x in file:
                self.adatok.append(x.strip(";"))


    def AlphaOrInt(self, list):  #Eldönti hogy szám vagy szöveg
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
                break
        
        aOi = ""
        if (s == len(list)):
            aOi = "string"
        if (i == len(list)):
            aOi = "int"
        if (barmi_mas == 1):
            aOi = "Hiba"

        return aOi
    
    def Input(self):
        print(r.AlphaOrInt(self.adatok)) # Valami hiba van az isalpha() résznél


r = Rendezés()
r.Input()