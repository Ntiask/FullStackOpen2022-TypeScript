from string import ascii_uppercase # <-- haetaan string kirjastosta ASCII uppercase joka sisältää kaikki kirjaimet ABCDEFHHJ jne ...

#print(ascii_uppercase) # <-- Tällä voit katsoa mitä tuo kirjasto pitää sisällään. tulostaa: ABCDEFGHIJKLMNOPQRSTUVWXYZ

def harpake(plop): # <-- plop on tässä tapauksessa alapuolella kutsuttaessa annettu numero esim 26
    lopputulos = [] # tyhjä lista?  yllärii :D
    assert 2<=plop<=26, 'Väärä Numero' # assert komennolla voidaan tehdä nopea if lause.  jos plop ei ole 2 ja 26 välillä niin palautetaan "Väärä Numero"
    for i in range(plop):  # jokaista numeroa kohden alkaen 0:sta annettuun ploppiin asti tehdään alla oleva lohko koodia
        for k, merkit in enumerate(lopputulos): # enumerate luo listan tavaroista tupleja esim (1: A), (2, B) 
            lopputulos[k] = ascii_uppercase[i] + merkit + ascii_uppercase[i] # Ascii merkeistä a:sta i variableen asti molemmille puolille.
        lopputulos.append((2*i+1)*ascii_uppercase[i]) # Lisätään lopputulokseen rivi joka sisältää oikeat merkit juuri tälle riville.

        if i != 0: # Lisätään lopputulokseen viimeinen ja ensimmäinen rivi koska ne ovat samat esim CCC ja CCC
            lopputulos.insert(0, (2*i+1)*ascii_uppercase[i]) 
            
    # print lopputulos ulos.
    for rivi in lopputulos:
        print(rivi)

harpake(int(input('Kerrokset: ')))
