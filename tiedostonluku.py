def suurin():
    with open("luvut.txt") as tiedosto: # <-- avataan tiedosto ? no shit sherlock :D
        isoin = 0 # määritetään luku mikä me palautetaan sittenkun sellainen löydetään ja sille alkuluku 0
        for rivi in tiedosto:  # Loopataan läpi jokainen tiedoston rivi
            rivi = int(rivi.replace("\n", "")) # muutetaan niin ettei rivissä ole rivinvaihtoa
            if rivi > isoin:
                isoin = rivi
        return isoin



def lue_hedelmat():
    sanakirja = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(";")
            sanakirja[rivi[0]] = float(rivi[1])
        return sanakirja

def summa():
    x=[]
    with open('matriisi.txt') as tiedosto:
        lista = []
        summa = 0
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(",")
            for i in rivi:
                lista.append(i)
        for x in lista:
            summa += int(x)
        return summa

def maksimi():
    x=[]
    with open('matriisi.txt') as tiedosto:
        lista = []
        suurin = 0
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(",")
            for i in rivi:
                lista.append(i)
        for x in lista:
            if int(x) > suurin:
                suurin = int(x)
        return suurin


def rivisummat():
    x=[]
    with open('matriisi.txt') as tiedosto:
        lista = []
        summa1 = 0
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(",")
            for i in rivi:
                summa1 += int(i)
            lista.append(summa1)
            summa1 = 0
        return lista
        

