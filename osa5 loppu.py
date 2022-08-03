
def lisaa_opiskelija(plop, nimi): #osa 1 alkaa
    plop[nimi] = []  #

def tulosta(plop1, nimi1):
    ka = []
    if nimi1 not in plop1:
        print(f"ei löytynyt ketään nimellä {nimi1}")
        return None
    if plop1[nimi1] == []:
        print(f"{nimi1}:")
        print(" ei suorituksia")

    if nimi1 in plop1 and plop1[nimi1]!= []:
        print(f"{nimi1}:")
        print(f" suorituksia {len(plop1[nimi1])} kurssilta:")
        for i in plop1[nimi1]:
            print(f"  {i[0]} {i[1]}")
            ka.append(i[1])
        print(" keskiarvo", sum(ka)/len(ka))
    

def lisaa_suoritus(opiskelijat, tyyppi, kurssi): #osa 2 alkaa
    kurssiennimet = []
    for i in opiskelijat[tyyppi]: # <-- käydään läpi opiskelijan (tyyppi) kurssit lista. OSA 3 ALKAA
        kurssiennimet.append(i[0])  # <-- kerätään opiskelijan kurssien nimet listaan. (osa2:n koodia loput osa3)

    if kurssi[1] != 0 and kurssi[0] not in kurssiennimet: # <-- katsotaan onko kurssin arvosana 0 tai jos kurssi löytyy jo listalta.
        opiskelijat[tyyppi].append(kurssi) # <-- jos näin on niin lisätään kurssi listalle
    if kurssi[0] in kurssiennimet: # <-- toinen skenaario.  jos kurssin nimi on jo kurssienlistalla
        for i in opiskelijat[tyyppi]: # <-- käydään kurssit läpi yksitellen
            if kurssi[0] == i[0]: # <-- etsitään nimeä vastaava kurssi  huom että tuplet ovat muotoa (0 = Kurssi, 1 = Arvosana)
                if kurssi[1] > i[1]: # <-- Katsotaan onko kurssin arvosana suurempi kuin aiemmin annettu numero
                    opiskelijat[tyyppi].remove(i) # <-- jos on, poistetaan nykyinen
                    opiskelijat[tyyppi].append(kurssi) # <-- Ja lisätään uusi.

def kooste(opiskelijat): # <-- OSA4 ALKAA
    keskiarvot = {}   # <-- Tehdään tyhjä keskiarvot sanakirja
    for key,value in opiskelijat.items(): # <-- luetaan jokainen avain sekä data opiskelijat sanakirjasta.
        summa=0 # määritetään että summa on aluksi 0
        for i in value: # käsitellään yksitellen jokaisen opiskelijan suoritus lista
            summa += i[1] # lisätään suoritusten arvosanat summaan
        average = summa/len(value) # <-- lasketaan keskiarvo summan ja listan pituuden avulla.
        keskiarvot[key] = average # <-- lisätään keskiarvot sanakirjaan henkilön nimi ja dataksi annetaan laskettu keskiarvo

    enitenSuorituksia = max(opiskelijat, key=lambda k: max(opiskelijat[k]))
    # <-- lasketaan eniten suorituksia saanut henkilö. 
    # tämän yllä oleva tekee samaa kuin alla oleva mutta käyttää vaan lambda 
    # funktiota laskennassa joka helpottaa asiaa huomattavasti
    '''largest = 0
        for key in opiskelijat.keys():
            if len(opiskelijat[key]) > largest:
                largest = (len(opiskelijat[key]))
                keys = key
                print(key, largest)'''
    

    print(f"opiskelijoita {len(opiskelijat)}")
    print(f"eniten suorituksia {len(opiskelijat[enitenSuorituksia])} {enitenSuorituksia}")
    print(f"paras keskiarvo {max(keskiarvot.values())} {max(keskiarvot, key=keskiarvot.get)} ")
    
if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    lisaa_suoritus(opiskelijat, "Liisa", ("asd", 4))
    lisaa_suoritus(opiskelijat, "Liisa", ("asdasdad", 4))
    tulosta(opiskelijat, 'Pekka')
    kooste(opiskelijat)
