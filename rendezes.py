class Rendezés:
    def Beolvas(self, allomanynev):  #Beolvassuk a ki.txt
        self.alap = []
        with open(allomanynev, "r", encoding="UTF8") as file:
           self.alap = file.read().split(";")
        del self.alap[-1]
        


    def AlphaOrInt(self, list):  #Eldönti hogy szám vagy szöveg    
        i = 0
        I = True
        s = 0
        S = True
        barmi_mas = 0
        for x in list:
            y = ''.join(x)
            try:
                if y.startswith('-'): #Negatív számokat is int-ként kezeli
                    int(y[1:])
                else:
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
    

    def SortInt(self, numbers): #Valami teljesen gatya itt
        
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if (numbers[i] > numbers[j]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers
        

    def Input(self):
        print(r.AlphaOrInt(self.alap))
        #print(r.SortInt(self.adatok))
       


r = Rendezés()
r.Beolvas("ki.txt")
r.Input()
