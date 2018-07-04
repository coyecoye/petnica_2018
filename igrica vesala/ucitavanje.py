import random 

#print(crtice)

def izaberi ():
    slovo = input ("Izaberi karakter:")
    return (slovo)

#print(izaberi())
    
def pogadjanje (rec,brSlova,slovo):
    ponavljanje = 0
    lista_indexa = []
    for i in range(0, (brSlova - 1)):
        if slovo == rec[i]:
            ponavljanje += 1
            lista_indexa.append(i)
    return lista_indexa, ponavljanje

#OVDE KRECE GLAVNI PROGRAM    

#ucitavamo recnik
f = open("recnik.txt")
reci = []
for s in f:
    reci.append(s)

#izaberi random rec
rec = random.choice(reci)
brSlova = len(rec)
rec1 = list(rec)

#postavi zivote
zivoti = 8

#postavi pocetni broj pogodjenih slova
pogodjeno= 0

#postavi crtice
crtice =  list("_"*(brSlova-1))
#print(rec)

while (zivoti>0):
   
    print("Trenutni broj zivota je: "  + str(zivoti) )
    slovo = izaberi()
    lista_indexa, ponavljanje = pogadjanje (rec,brSlova,slovo)
    
    if ponavljanje == 0:
        print("progresio si")
        zivoti -= 1
    
    if zivoti ==0:
        print("izgubio si")
        exit()

    if ponavljanje > 0:
        print("pogodio si")
        ponavljanje += 1
    
    if ponavljanje > 0:
        for i in lista_indexa:
            crtice[i] = slovo
    print(crtice)

    if "_" not in crtice:
        print("pobedio si")
        exit()