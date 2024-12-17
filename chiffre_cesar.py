import string 

def chiffre_cesar (chaine: str, decalage: int):
    alphabet = string.printable
    chiffrage = ""

    for i in chaine:
        if i in alphabet:
            nombre = (alphabet.index(i) + decalage) % 100
            chiffrage += alphabet[nombre]
    return chiffrage

print (chiffre_cesar("Coucou", 5))

def dechiffre_cesar(chaine, decalage):
    return chiffre_cesar(chaine,-decalage)

print (dechiffre_cesar("Htzhtz", 5))

def brute_force(message):
    possibilite = ""
    clef = 100
    for i in range (0,clef):
        possibilite = dechiffre_cesar(message,clef)
        print(dechiffre_cesar(message, clef))
    return possibilite

brute_force("Quiero hacerte el amor")
    


