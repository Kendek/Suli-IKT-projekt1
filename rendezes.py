class Rendezés:
    def __init__(self, allomanynev):  #Beolvassuk a ki.txt
        self.adatok = []
        with open(allomanynev, "r", encoding="UTF8") as file:
            for x in file:
                self.adatok.append(x.strip(";").split(";"))


    def AlphaOrInt(self, list):  #Eldönti hogy szám vagy szöveg
        i = 0
        I = True
        s = 0
        S = True
        barmi_mas = 0
        for x in list:
            y = ''.join(map(str, x))
            try:
                int(y)
            except ValueError:
                I = False
            if (I):
                i += 1
            else:
                u = y.isalpha()
                if (u):
                    s += 1
                else:
                    barmi_mas += 1
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
        print(r.AlphaOrInt(self.adatok)) 


r = Rendezés("ki.txt")
r.Input()
