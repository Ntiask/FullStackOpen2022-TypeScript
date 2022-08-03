def hae_raakaaine(osoite, raakaaine):
    nimet = []
    with open(osoite) as tiedosto:
        lista = []
        sisalto = tiedosto.read()
        reseptilista = sisalto.replace("\n\n", ",").split(',')
        for i in reseptilista:
            lista.append(i.replace("\n", ",").split(","))
    
    for i in lista:
        for x in range(2, len(i)):
            if i[x] == raakaaine:
                nimet.append(f"{i[0]}, valmistusaika {i[1]} min")
    return nimet


loydetyt = hae_raakaaine("reseptit1.txt", "maito")

for resepti in loydetyt:
    print(resepti)