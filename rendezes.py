class Rendezés:
    def Beolvas(self, allomanynev):  #Beolvassuk a ki.txt
        self.alap = []
        with open(allomanynev, "r", encoding="UTF8") as file:
           self.alap = file.read().split(";")
        del self.alap[-1]  #Alap lista, kivettem az üres sort
        
        self.split = []
        for x in self.alap:
            self.split.append(x.strip("-"))


    def AlphaOrInt(self, list):  #Eldönti hogy szám vagy szöveg    
        i = 0
        I = True
        s = 0
        S = True
        barmi_mas = 0
        for x in list:
            y = ''.join(x)
            try:     
                int(y)
            except ValueError:
                I = False
            if (I):
                i += 1
            else:
                S = y.isalpha()
                if (S):
                    s += 1
                else:
                    barmi_mas += 1
                    break

        if (s == len(list)):
            return "string"
        if (i == len(list)):
            return "int"
        if (barmi_mas == 1):
            return "Hiba"
    

    def Listak(self):   #Külön listát csinál ha int vagy ha string

        msg = r.AlphaOrInt(self.split)
        self.szoveg = []
        self.szam = []

        if (msg == "string"):
            for x in self.alap:
                self.szoveg.append(x)

        if (msg == "int"):
            for x in self.alap:
                self.szam.append(int(x))

        if (msg == "Hiba"):
            print("Hibás a fájl beviteli karakterlánca!")

    def SimpleSortInt(self, lst): #Valami teljesen gatya itt
        
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if (lst[i] > lst[j]):
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
    
    def SimpleSortStr(self, lst):
       
        for w in range(len(lst)):
            lst[w] = lst[w].lower()

        for n in range(len(lst)-1, 0, -1):
            for i in range(n):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
        
        return lst


    def Input(self):    #Teszt function
        print(r.AlphaOrInt(self.split))
        #print(r.SimpleSortInt(self.szam))
        print(r.SimpleSortStr(self.szoveg))
       
       


r = Rendezés()
r.Beolvas("ki.txt")
r.Listak()

r.Input()
