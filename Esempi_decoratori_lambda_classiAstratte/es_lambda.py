#trasformo in lambda le funzioni della classe Paroliere
import numpy as np

unisci_parole = lambda p1,p2: p1+p2
separa_parole = lambda stringa: stringa.split()
rimuovi_parole = lambda stringa, parola: [elemento for elemento in stringa if elemento != parola]
trova_parole = lambda stringa, parola: True if parola in stringa else False 
randomizza_parola_in_lista = lambda lista: lista[np.random.randint(len(lista))]

lista_animali = ["cane", "gatto", "cane","cervo","canguro"]
print(unisci_parole("ci","ao"))
print(separa_parole("Il sole è splendente"))
lista_senza_cane = rimuovi_parole(lista_animali, "cane")
print(lista_senza_cane)
print(trova_parole(lista_animali, "gatto"))
print(randomizza_parola_in_lista(lista_animali))