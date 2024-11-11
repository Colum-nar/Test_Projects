"""
classe magazzino, classe prodotto
classe magazzino
una lista che contiene i prodotti
una funzione che ricerca i prodotti, ritorna il prodotto ricercato 
funzione che fa vedere il magazzino attraverso la stampa dei prodotti
funzione che aggiunge il prodotto

la classe prodotto : prezzo, quantita, codice, nome
nel momento in cui andiamo a inizializzare i 4 attribuiti associamo a ciascuno di essi un metodo che controllera la loro validita se necessario
fatto cio andiamo ad aggiungere il prodotto alla lista
permettere l ingresso di nuovi prodotti
opzione per uscire


"""
#funzione che mostra le scelte  disposizione dell'utente, ritorna la scelta dell'utente
def mostra_scelte():
    scelta = input("""
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantita di un prodotto
Invia 4 se vuoi modificare il nome di un prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l inventario
Invia 7 se vuoi verificare se un prodotto è presente o meno nel magazzino e vedere le sue caratteristiche
Invia 8 se vuoi uscire dal programma (attenzione perderai i dati del magazzino)
>>> """)
    return scelta
#classe che ha 2 attributi il nome e la lista dei prodotti 
class Magazzino():
    def __init__(self, nome = "magazzino"): # costruttore, , prende due parametri: l'ggetto stesso e il nome del magazzino, parametro che ha un valore di default
        self.nome = nome
        self.prodotti = []

    #mostra i prodotti all interno della lista attraverso il metodo speciale str
    def mostra_prodotti(self):
        for prodotto in self.prodotti:
            print(prodotto)
            print("---")
        input("premi invio per continuare ")
    #aggiungiamo il prodotto dentro la lista
    def aggiungi_prodotto(self, prodotto): 
        self.prodotti.append(prodotto)
    # - facciamo un matching tra nome messo dell utente e nomi dei prodotti presenti nell omonima lista
    def ricerca_prodotto(self): 
        nome_da_ricercare = input("Inserisci il nome del prodotto: ")
        #ritorniamo il prodotto se il matching da esito positivo, altrimenti segnaliamo l'esito negativo all utente e ritorniamo false
        for prodotto in self.prodotti:
            if prodotto.nome.lower() == nome_da_ricercare.lower():
                print(prodotto)
                input("premi invio per continuare: ")
                return prodotto
            
        print("Prodotto non trovato")
        input("\nPremi Invio per continuare: ")
        return False

    def __len__(self): #metodo speciale
        return len(self.prodotti) #implementazione del metodo speciale, restotuisce la lunghezza della lista

class Prodotto():
    def __init__(self, nome, prezzo, quantita, codice, magazzino):
        self.nome = nome
        self.modifica_inserisci_prezzo(prezzo)
        self.modifica_inserisci_quantita(quantita)
        self.codice = codice
        magazzino.aggiungi_prodotto(self)
        
    def modifica_nome(self, nome):
        self.nome = nome
        print("Nuovo nome inserito ", self.nome)
    #controlla che il dato sia superiore a 0
    def modifica_inserisci_prezzo(self, prezzo):
        while True:
            try: #prova a covertire in float il valore e lo arrotonda alla seconda cifra decimale, se da errore chiama il codice sotto l except
                prezzo = round(float(prezzo), 2)
                if prezzo > 0:
                    self._prezzo = prezzo
                    break
                else:
                    print("Il prezzo deve essere maggiore di 0")
                    prezzo = input("Inserisci un numero maggiore di 0\n>>>")
            except ValueError:
                print("Input non valido")
                prezzo = input("Inserisci un numero maggiore di 0\n>>>")
    def modifica_inserisci_quantita(self, quantita): #-verifica che il dato inserito sia un intero maggiore o uguale a 0 
        while True:
            try: #prova a covertire in intero il valore se da errore chiama il codice sotto l except
                quantita = int(quantita)
                if quantita >= 0:
                    self._quantita = quantita
                    break
                    
                else:
                    print("La quantita deve essere maggiore o uguale a 0")
                    quantita = input("Inserisci un numero intero maggiore o uguale a 0\n>>>")
            except ValueError:
                print("Input non valido")
                quantita = input("Inserisci un numero intero maggiore o uguale a 0\n>>>")

    def modifica_codice(self, codice):
        self.codice = codice
        print("Nuovo codice inserito: ",self.codice)
    
    def __str__(self): # metodo speciale str, viene chiamato quando printiamo un prodotto
        return  f"""Nome:     {self.nome}
Prezzo:   {self._prezzo}
Quantita: {self._quantita} 
Codice:   {self.codice}"""


# - - - - - - - - - - -

#creiamo un oggetto magazzinp
mag = Magazzino()
scelta_utente = 0
while scelta_utente != "8":
    scelta_utente = mostra_scelte()
    #Vero se __len__() restituisce un valore diverso da 0.
    if not mag and scelta_utente != "1": #se nessun prodotto all'interno del magazzino ne forziamo l'inserimento
        print("Magazzino vuoto, inserisci almeno un prodotto per poter usufruire delle funzionalità del programma")
        scelta_utente = "1"
    if scelta_utente == "1":
        print("Inserimento nuovo prodotto")
        nome = input("Inserisci il nome del prodotto: ")
        pz = input("Inserisci il prezzo del prodotto: ")
        qt = input("Inserisci la quantità del prodotto: ")
        codice = input("Inserisci il codice del prodotto: ")
        #creiamo un oggetto della classe Prodotto con i dati inseriti dall'utente
        prod = Prodotto(nome, pz, qt, codice, mag)
    elif(scelta_utente == "2"):
        prodotto = mag.ricerca_prodotto()
        #falso se non trova il prodotto
        if prodotto: #Se non sono presenti né __bool__() né __len__() all interno della classe, l'oggetto è sempre considerato vero.
            prezzo = input("Inserisci il nuovo prezzo: ")
            prodotto.modifica_inserisci_prezzo(prezzo)
    elif(scelta_utente == "3"):
        prodotto = mag.ricerca_prodotto() 
        #falso se non trova il prodotto
        if prodotto: #Se non sono presenti né __bool__() né __len__() all interno della classe, l'oggetto è sempre considerato vero.
            quantita = input("Inserisci la nuova quantità: ")
            prodotto.modifica_inserisci_quantita(quantita)                
    elif(scelta_utente == "4"):
        prodotto = mag.ricerca_prodotto() 
        #falso se non trova il prodotto
        if prodotto: #Se non sono presenti né __bool__() né __len__() all interno della classe, l'oggetto è sempre considerato vero.
            nome = input("Inserisci il nuovo nome: ")
            prodotto.modifica_nome(nome)
    elif(scelta_utente == "5"):
        prodotto = mag.ricerca_prodotto() 
        #falso se non trova il prodotto
        if prodotto: #Se non sono presenti né __bool__() né __len__() all interno della classe, l'oggetto è sempre considerato vero.
            codice = input("Inserisci il nuovo codice: ")
            prodotto.modifica_codice(codice)
    elif(scelta_utente == "6"):#mostra i prodotti dentro al magazzino 
        mag.mostra_prodotti()
    elif(scelta_utente == "7"):#ricerca un prodotto in magazzino sulla base del nome
        mag.ricerca_prodotto()
    elif(scelta_utente == "8"):
            #si chiude il programma
        print("Programma in chiusura")
        break 