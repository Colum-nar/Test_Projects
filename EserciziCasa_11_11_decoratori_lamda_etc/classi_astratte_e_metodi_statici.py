#classe astratta animale
#classe paroliere
#usati staticmethob e abstractmethod

import numpy as np




class Paroliere:
    @staticmethod
    def unisci_parole(word1, word2):
        return word1+word2
    @staticmethod
    def separa_parole(stringa):
        return stringa.split()
    @staticmethod
    def trova_parole(lista_stringhe, parola_da_trovare):
        if parola_da_trovare in lista_stringhe:
            return True
        else:
            return False
    @staticmethod
    def rimuovi_parole(lista_stringhe, parola_da_eliminare):
        contatore = lista_stringhe.count(parola_da_eliminare)
        i = 0
        while contatore != i:
            lista_stringhe.remove(parola_da_eliminare)
            i += 1
    @staticmethod
    def randomizza_parola_in_lista(lista_stringhe):
        n = len(lista_stringhe)
        n = np.random.randint(n)
        return lista_stringhe[n]
        
lista_animali = ["cane", "gatto", "cane","cervo","canguro"]
print(Paroliere.unisci_parole("parola_", "unita"))
print(Paroliere.separa_parole("Il sole è splendente"))
print(Paroliere.trova_parole(["cane","gatto","cavallo"], "cane"))
Paroliere.rimuovi_parole(lista_animali, "cane")
print(lista_animali)

print(Paroliere.randomizza_parola_in_lista(lista_animali))
    
    
    
    
    
    
    
    
from abc import ABC, abstractmethod
class Animale(ABC):
    @abstractmethod
    def riposare(self):
        """L'animale si riposa per recuperare le forze per attaccare"""
        """riposare abbassa le difese per quel turno"""
        pass
    @abstractmethod
    def attacca(self):
        """l'animale deve attaccare altri animali per sopravvivere"""
        """attaccare consuma energie che possono essere recuperate riposando"""
        pass
class Noctwolf(Animale):
    nome_classe = "Noctwolf"

    def __init__(self, nome):
        self.nome = nome
        self.attacco = np.random.randint(10, 21)
        self.difesa = np.random.randint(5,11)
        self.vita = 90
        self.energia = 50
    def descrivi_essere(cls): #metodo di classe
        print(cls.nome_classe, "è un animale a cui piace l'oscurità.\nGli antichi credevano che durante la luna piena avesse poteri sovrannaturali.")
    def attacca(self):
        #il danno ha un range, ha il 5 per cento di fare un critico
        danni =  self.attacco + np.random.randint(-5,6) if np.random.randint(0,101) <= 95 else (self.attacco + np.random.randint(-5,6) ) * 1.5
        print(self.nome, " si lancia sulla preda con i suoi artigli affilati")
        self.energia -= 12
        print("Energia restante", self.energia)
        return danni
    def riposare(self):
        self.energia += 30
        print(self.nome, "si riposa. Energia totale:", self.energia)

print(Noctwolf.nome_classe)
Noctwolf.descrivi_essere(Noctwolf)
noct1 = Noctwolf("Ryzen")
print(noct1.attacca(), "danni inflitti")
noct1.riposare()



