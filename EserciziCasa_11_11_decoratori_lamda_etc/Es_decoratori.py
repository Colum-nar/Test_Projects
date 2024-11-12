#classe giocatore, blocchiamo l uso di determinati nomi e età attraverso le property
#creiamo una "variabile" dinamica salto attraverso l uso di property
#uso di decoratori personalizzati - creiamo una funzione battaglia e la decoriamo con misuratore_tempo per verificare quanto dura la battaglia 
#oltre a questo tempo fa fatto a casa esecizio cn la classe lottatore, il file si trova a lezione29_10 - si chiama property


import time
import numpy as np 

def misuratore_tempo(func):
    def wrapper(*args, **kwargs):
        inizio_battaglia = time.time() #il tempo a inizio della battaglia
        funzione = func(*args, **kwargs)
        fine_battaglia = time.time()#il tempo a fine battaglia
        print(f"Tempo della battaglia: {fine_battaglia - inizio_battaglia:.6f} secondi")
        return funzione
    return wrapper

class Giocatore:
    soldi = 10
    __parolacce_italiano = ["cazzo", "merda", "stronzo", "vaffanculo", "puttana", 
    "porco", "figa", "bastardo", "zoccola", "troia", 
    "imbecille", "deficiente", "coglione", "testa di cazzo", 
    "minchia", "sfigato", "puzzolente", "cornuto", "pezzo di merda"]
    def __init__(self, nome, età, velocita = 3, tempo_premuto_salto = 1, vita = 100, attacco = 10):
        self.nome = nome
        self._età = None # un underscore si riferisce a delle proprietà
        self.età = età  # usa il setter per la validazione
        self.velocita = velocita #li utilizzeremo per creare una "variabile" dinamica attraverso i decoratori
        self.tempo_premuto_salto = tempo_premuto_salto #li utilizzeremo per creare una variabile dinamica attraverso i decoratori
        self.vita = vita
        self.attacco = attacco
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valore):
        print("ciao")
        while True:
            if valore.lower() in self.__parolacce_italiano:
                print("Nome non valido")
                valore = input("Inserisci nuovo nome: ")
            else:
                self._nome = valore #crea o assegna valore ad attributo _nome
                break

    # Getter per l'attributo "età"
    @property
    def età(self):
        return self._età

    # Setter per l'attributo "età" con validazione
    @età.setter
    def età(self, valore):
        if valore >= 0:
            self._età = valore
        else:
            raise ValueError("L'età non può essere negativa")
    @property #creiamo una "variabile" dinamica attraverso l uso del property
    def salto(self):
        return f"{self.nome} salta {self.velocita * self.tempo_premuto_salto} metri"
    def attacca(self):
        attacco = self.attacco + np.random.randint(-5,6)
        return attacco
@misuratore_tempo
def scontro(giocatore1, giocatore2):
    if giocatore1.velocita > giocatore2.velocita:
        while giocatore1.vita > 0 and giocatore2.vita >0:
            danni_1g = giocatore1.attacca()
            giocatore2.vita -= danni_1g
            print(f"{giocatore1.nome} attacca {giocatore2.nome}, danni {danni_1g} vita restante {giocatore2.vita}")
            danni_2g = giocatore2.attacca()
            giocatore1.vita -= danni_2g
            print(f"{giocatore2.nome} attacca {giocatore1.nome}, danni {danni_2g} vita restante {giocatore1.vita}")

    else:
        while giocatore1.vita > 0 and giocatore2.vita >0:
            danni_2g = giocatore2.attacca()
            giocatore1.vita -= danni_2g
            print(f"{giocatore2.nome} attacca {giocatore1.nome}, danni {danni_2g} vita restante {giocatore1.vita}")
            danni_1g = giocatore1.attacca()
            giocatore2.vita -= danni_1g
            print(f"{giocatore1.nome} attacca {giocatore2.nome}, danni {danni_1g} vita restante {giocatore2.vita}")
    if giocatore1.vita > 0:
        print(giocatore1.nome, " ha vinto")
    else:
        print(giocatore2.nome, " ha vinto")
        
#- - - - - - - - - - - -- - - - - - - -
a = Giocatore("puzzolente", 5)#fa modificare il nome
print(a.salto)
#b = Giocatore("puzzolente", -5)#da errore
c = Giocatore ("Fabio", 10, velocita = 5)
print(c.salto)
c.nome = "puzzolente"
print(c.salto)

scontro(a,c)


