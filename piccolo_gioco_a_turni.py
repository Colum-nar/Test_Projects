


# ----- 
#un mostro ha rapito la principessa
#Il nostro eroe deve affrontare 4 suoi scagnozzi per arrivare a lui e salvare la principessa
#------

import random  # Importa la libreria random per la generazione casuale
import numpy as np  # Importa numpy, usato per operazioni numeriche avanzate
from abc import ABC, abstractmethod  # Importa la classe ABC e la funzione Abstractmethod per creare classi astratte

# Definizione di oggetti comuni e rari che possono essere trovati durante il gioco
oggetti_comuni = {"Pozione vita": 50, "Pozione energia": 50, "Pozione attacco": 5}
oggetto_raro = {"Pozione livello": 1}

# Funzione per applicare l'effetto dell'oggetto scelto 
def effetto_oggetto(scelta, eroe):
    if scelta == "Pozione vita":
        eroe.vita += oggetti_comuni["Pozione vita"]  # Aumenta la vita dell'eroe
    elif scelta == "Pozione energia":
        eroe.energia += oggetti_comuni["Pozione energia"]  # Aumenta l'energia dell'eroe
    elif scelta == "Pozione attacco":
        eroe.attacco += oggetti_comuni["Pozione attacco"] # Aumenta l'attacco dell'eroe
    else:
        eroe.livello += 1  # Aumenta il livello dell'eroe
        eroe.attacco += 50  # Aumenta l'attacco dell'eroe
        eroe.vita += 50  # Aumenta la vita dell'eroe
        eroe.energia += 50  # Aumenta l'energia dell'eroe

punteggio = 0  # Variabile globale per tenere traccia del punteggio

# Classe astratta per la gestione dei personaggi
class Personaggio(ABC):#classe che eredita da ABC
    #set di nomi inappropriati per un giocatore
    __nomi_inappropriati = {"cazzo", "merda", "stronzo", "vaffanculo", "puttana", 
                            "porco", "figa", "bastardo", "zoccola", "troia", 
                            "imbecille", "deficiente", "coglione", "testa di cazzo", 
                            "minchia", "sfigato", "puzzolente", "cornuto", "pezzo di merda"}
    # Costruttore di base per il nome del personaggio
    def __init__(self, nome):
        self.nome = nome #ritorna il valore dell'attributo
    #decoratore utilizzato per restituire e validare un valore secondo un criterio
    # Getter per il nome
    @property
    def nome(self):
        return self._nome

    # Setter per il nome, con controllo per nomi inappropriati
    @nome.setter
    def nome(self, valore):
        while True:
            if valore.lower() in self.__nomi_inappropriati:  # Se il nome è inappropriato fa inserire un altro nome
                print("Nome non valido")
                valore = input("Inserisci nuovo nome: ")
            else:
                self._nome = valore  # Imposta il nome valido
                break
    #utilizzo del decoratore abstractmethod, si lascia la sua implementazione alle classi figlio
    @abstractmethod
    def azioni(self):
        pass  # Metodo astratto per le azioni del personaggio

# Classe per l'eroe, derivata dalla classe Personaggio
class Eroe(Personaggio):
    #lista di dizionari con le mosse dell'eroe e il loro relativo costo e effetto
    mosse = [
        {"nome": "Fendente", "costo_energia": 10, "danno": 25},
        {"nome": "Riposo", "costo_energia": 0, "ripristino energia": 25},
        {"nome": "Cura", "costo_energia": 15, "recupero vita": 30}
    ]
    
    # Costruttore per l'eroe, con parametri di attacco, vita, energia, livello e inventario
    def __init__(self, nome, attacco=15, vita=100, energia=50, livello=1, inventario=None):
        super().__init__(nome)#Chiamiamo il costruttore della classe base Personaggio
        if inventario is None:
            inventario = []  
        self.attacco = attacco
        self.vita = vita
        self.energia = energia
        self.livello = livello
        self.inventario = inventario


    # Permette all'eroe di scegliere un oggetto dall'inventario
    def scegli_da_inventario(self):
        if self.inventario:
            trovato = False
            scelta = input("Inserisci il nome dell'oggetto: ")
            if scelta in self.inventario:
                effetto_oggetto(scelta, self)  # chiamiamo il metodo effetto_oggetto per usare l effetto di oggetto
                self.inventario.remove(scelta)  # Rimuove l'oggetto dall'inventario
                print("Oggetto trovato")
                trovato = True
            if not trovato:
                print("Oggetto non trovato")
        else:
            print("inventario vuoto")

    # Mostra tutti gli oggetti nell'inventario dell'eroe
    def mostra_inventario(self):
        for oggetto in self.inventario: #mostra gli oggetti nell'inventario iterando l inventaro
            print(oggetto)

    # Mostra le mosse dell'eroe
    def mostra_mosse(self):
        i = 1
        for mossa in self.mosse:
            print(i, end="") #con il parametro end = "" diciamo di continuare a stampare sulla stessa riga
            for chiave, valore in mossa.items():
                print(f" {chiave}: {valore}", end="")  # Stampa le caratteristiche della mossa su una sola riga
            print("")
            i += 1

    # Permette all'eroe di scegliere una mossa
    def scegli_mosse(self):
        
        while True: #finchè l utente non inserisce un valore convertibile in un intero
            self.mostra_mosse() #chiamiamo il metodo mostra_mosse
            scelta = input("Scegli la mossa da usare: ")
            try:#verifichiamo che abbia inserito un numero intero
                scelta = int(scelta) #a seconda del numero inviato esegue una mossa
                if 1 <= scelta <= len(self.mosse): #se il numero è nel range 1 - 3
                    mossa_scelta = self.mosse[scelta - 1] #salviamo dizionario relativo all'abilità scelta in mossa_scelta
                    print(f"Hai scelto: {mossa_scelta['nome']}") 
                    return mossa_scelta #ritorniamo il dizionario
                else:
                    print("Scelta non valida.")
                    return None #se numero non valido ritorniamo None
            except:#se input non convertibile in un intero
                print("Input non corretto")

    # Calcola e restituisce il danno dell'attacco dell'eroe
    def attacca(self):
        danno = self.attacco + np.random.randint(-5, 6)  # aggiungiamo variabilità nell'attacco
        return danno #ritorniamo il danno

    # Permette all'eroe di eseguire azioni contro un nemico
    def azioni(self, nemico): #richiede un oggetto eroe e uno nemico
        scelta = input(f"Sei davanti a {nemico.nome}. Cosa vuoi fare? (1 = Abilità, 2 = Inventario): ")
        if scelta == "1":
            mossa = self.scegli_mosse() #mostra e fa scegliere le mosse
            if mossa and mossa["costo_energia"] <= self.energia: #se l'energia dell eroe è sufficiente e mossa non è None
                self.energia -= mossa["costo_energia"]#sottraiamo l energia della mossa
                if "danno" in mossa:#se la mossa fa danno
                    danno_inflitto = self.attacca() + mossa["danno"] # sommiamo il danno della mossa al danno di attacca()
                    nemico.vita -= danno_inflitto #spttraiamo al nemico la vita
                    print(f"{self.nome} infligge {danno_inflitto} danni a {nemico.nome}.") #stampiamo cio che è successo
                elif "recupero vita" in mossa: #se la mossa ha una chiave recupero vita
                    self.vita += mossa["recupero vita"] #allora la vita viene recuperata del valore 
                    print(f"{self.nome} recupera {mossa['recupero vita']} punti vita.")
                elif "ripristino energia" in mossa: #se la mossa ha una chiave recupero energia 
                    self.energia += mossa["ripristino energia"]#allora viene recurperata energia
                    print(f"{self.nome} ripristina {mossa['ripristino energia']} punti vita.")

                    
            else:
                print("Energia insufficiente.")
        elif scelta == "2":
            self.mostra_inventario() #mostra l inventario
            self.scegli_da_inventario() # fa scegliere e chiama il metodo per usare l effetto dell'oggetto

# Classe per i nemici, figlia della classe Personaggio
class Nemico(Personaggio):
    nomi_possibili = {"Dragan", "Orcun", "Trollo", "Scheletrox", "Goblinius"}
    #lista di dizionari con le mosse dei nemici
    mosse = [
        {"nome": "Carica bestiale", "costo_energia": 10, "danno": 20},
        {"nome": "Morso", "costo_energia": 5, "danno": 15},
        {"nome": "Lancio pietre", "costo_energia": 0, "danno": 5}
    ]

    # Costruttore per il nemico, con nome e attributi casuali sulla base di determinati valori
    def __init__(self):
        nome = random.choice(list(self.nomi_possibili))
        Nemico.nomi_possibili.discard(nome)  # Rimuove il nome scelto dalla lista, 2 mostri non possono avere lo stesso nome
        super().__init__(nome)
        self.attacco = random.randint(5, 10)
        self.vita = random.randint(50, 80)
        self.energia = random.randint(30, 50)  

    # Viene scelta una mossa casuale per il nemico
    def scegli_mossa(self):
        #uso di filter con una funzione lambda
        abilita_utilizzabili = list(filter(lambda x: x["costo_energia"] <= self.energia, self.mosse)) #il nemico potrà usare solo una mossa che non oltrepassi la sua energia attuale
        mossa = random.choice(abilita_utilizzabili)#si randomizza la scelta tra le mosse effettuabile dal nemico
        self.energia -= mossa["costo_energia"]#si riduce l'energia
        return mossa #si ritorna il dizionario con la mossa
    def attacca(self):
        danno = self.attacco + np.random.randint(-5, 6)  # aggiungiamo variabilità nell'attacco
        return danno #ritorniamo il danno
    # Azioni del nemico durante la battaglia
    def azioni(self, eroe):
        mossa = self.scegli_mossa()
        if "danno" in mossa: #se danno presente come chiave
            danno_inflitto = self.attacca() + mossa["danno"] 
            print(f"{self.nome} sceglie la mossa {mossa['nome']} che infligge {danno_inflitto} danni.")
            print(f"{self.nome} infligge {danno_inflitto} danni a {eroe.nome}.") #stampiamo cio che è successo
            print(f"{self.nome} ha {self.energia} energia")
            eroe.vita -= danno_inflitto
        else:#altrimenti
            self.energia += mossa["ripristino energia"]# viene recurperata energia
            print(f"{self.nome} ripristina {mossa['ripristino energia']} punti energia.")

    # Rilascia un oggetto comune dopo essere stato sconfitto
    def rilascia_oggetto(self):
        global punteggio # variabile globale
        punteggio += 10 #aumenta il punteggio di 10
        return random.choice(list(oggetti_comuni.keys()))


# Classe per il boss, derivata dalla classe Nemico
class Boss(Nemico):
    #mosse specifiche per il boss
    mosse = [
        {"nome": "Urlo Infernale", "costo_energia": 20, "danno": 40},
        {"nome": "Terremoto", "costo_energia": 15, "danno": 35},
        {"nome": "Recupero Energie", "costo_energia": 0, "ripristino energia": 50}
    ]
    #costruttore che chiama il costruttore della classe madre e modifica gli attributi di base
    def __init__(self):
        super().__init__()
        self.attacco += 10
        self.vita += 40

    # Rilascia un oggetto raro dopo essere stato sconfitto
    def rilascia_oggetto_raro(self):
        global punteggio #ci riferiamo alla variabile globale
        punteggio += 20 # aumenta il punteggio di 20
        return "Pozione livello"

# Funzione per gestire una battaglia tra l'eroe e un nemico
def battaglia(eroe, nemico):
    while eroe.vita > 0 and nemico.vita > 0: #finche sia l eroe che il nemico sono in vita
        print(f"{eroe.nome} ha {eroe.vita} punti vita e {eroe.energia} energia, {nemico.nome} ha {nemico.vita} punti vita.")
        
        eroe.azioni(nemico) #chiamiamo il metodo azioni che permette all utente di scegliere che mossa effettuare
        
        if nemico.vita <= 0: #se vita nemico inferiore o uguale a 0
            print(f"{nemico.nome} è stato sconfitto!")
            oggetto_rilasciato = nemico.rilascia_oggetto()  # Oggetto rilasciato dal nemico
            print(f"{nemico.nome} ha rilasciato {oggetto_rilasciato}.")
            eroe.inventario.append(oggetto_rilasciato)  # Aggiunge l'oggetto all'inventario dell'eroe
            print(punteggio, "punteggio attuale.")
            print("--------")
            break

        nemico.azioni(eroe) #facciamo agire il nemico
        if eroe.vita <= 0: #se la vita è minore o uguale a 0
            print(f"{eroe.nome} è stato sconfitto!")
            print(punteggio, "punteggio finale.")
            break

# - * - * - * - * - * - * - * - * - * 

nome = input("Scegli il nome del tuo eroe: ")
eroe = Eroe(nome) #creiamo L'eroe
nemici = [Nemico() for _ in range(4)]  # Creiamo 4 nemici e li mettiamo in una lista
boss = Boss() #creiamo il Boss

# Eroe affronta i nemici uno dopo l'altro
for nemico in nemici:
    battaglia(eroe, nemico)

# Affronta il boss se l'eroe è ancora in vita
if eroe.vita > 0:
    print("SEI DAVANTI AL BOSS CHE HA RAPITO LA PRINCIPESSA")
    battaglia(eroe, boss)
if boss.vita <= 0:
    print("Hai sconfitto il boss, la principessa è SALVA!!!")
