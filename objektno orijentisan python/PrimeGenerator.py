import math as m
 
class PrimeGenerator:
    def __init__(self):
        self.pocetni = 2
    def getBroj(self):
        return self.pocetni
    def prostBroj(self):
        i = 2
        da = True
        while i <= m.sqrt(self.pocetni) and da:
            if self.pocetni % i == 0:
                da = False
            i += 1
        return da
    def next(self):
        self.pocetni += 1
        while not self.prostBroj():
            self.pocetni += 1
        return self
 
a = PrimeGenerator()
 
print(a.getBroj())
 
print(a.next().getBroj())

print(a.next().getBroj())