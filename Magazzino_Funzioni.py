

# Funzione che mostra gli oggetti nel magazzino
def modifica_o_inserisci_codice(prodotto):
    if prodotto == []:
        print("La modifica non può essere effettuata")
        return
    if prodotto["codice"] == "":
        # Chiediamo all'utente di inserire il codice
        nuovo_codice = (input(f"Inserisci il codice  per il prodotto '{prodotto['nome']}': "))
        prodotto['codice'] = nuovo_codice
        print(f"codice per '{prodotto['nome']}' inserita: {prodotto['codice']}")
        input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
        return prodotto
    else:
        # Mostriamo il codice attuale e chiediamo se vogliono modificarlo
        print(f"codice attuale di '{prodotto['nome']}': {prodotto["codice"]}]")
        modifica = input("Vuoi modificare il codice ? (s/n): ")
        if modifica.lower() == 's':
            nuovo_codice = (input(f"Inserisci il  nuovo codice per il prodotto '{prodotto['nome']}': "))
            prodotto['codice'] = nuovo_codice
            print(f"codice per '{prodotto['nome']}' aggiornata a: {prodotto['codice']}")
            input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
        else:
            print("Nessuna modifica effettuata.")
def mostra_magazzino(magazzino):
    print("Oggetti nel magazzino:")
    for dizionario in magazzino:
        for chiave, valore in dizionario.items():
            print(f"- {chiave}: {valore}")
        input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 


# Esegui la funzione per vedere gli oggetti nel magazzino

# Funzione per modificare o inserire il prezzo di un prodotto
def modifica_o_inserisci_prezzo(prodotto):
    if prodotto == []:
        print("La modifica non può essere effettuata")
        return
    # Se il prezzo è 0, chiediamo all'utente di inserirlo per un nuovo prodotto
    if prodotto["prezzo"] == 0:
        while True:  # Ciclo per assicurarsi che l'input sia valido
            nuovo_prezzo = input(f"Inserisci il prezzo per il prodotto '{prodotto['nome']}': ")
            try:
                # Controlliamo che l'input sia un numero valido
                nuovo_prezzo_float = float(nuovo_prezzo)
                if nuovo_prezzo_float >= 0:
                    prodotto['prezzo'] = nuovo_prezzo_float
                    print(f"Prezzo per '{prodotto['nome']}' inserito: {prodotto['prezzo']:.2f}")
                    input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
                    return prodotto
                    break
                else:
                    print("Il prezzo non può essere negativo.")
            except ValueError:
                print("Prezzo non valido. Inserisci solo numeri (es. 12 o 12.99).")
    else:
        # Mostriamo il prezzo attuale e chiediamo se vogliono modificarlo
        print(f"Prezzo attuale di '{prodotto['nome']}': {prodotto['prezzo']:.2f}")
        modifica = input("Vuoi modificare il prezzo? (s/n): ")
        if modifica.lower() == 's':
            while True:
                nuovo_prezzo = input(f"Inserisci il nuovo prezzo per il prodotto '{prodotto['nome']}': ")
                try:
                    nuovo_prezzo_float = float(nuovo_prezzo)
                    if nuovo_prezzo_float >= 0:
                        prodotto['prezzo'] = nuovo_prezzo_float
                        print(f"Prezzo per '{prodotto['nome']}' aggiornato a: {prodotto['prezzo']:.2f}")
                        input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
                        break
                    else:
                        print("Il prezzo non può essere negativo.")
                except ValueError:
                    print("Prezzo non valido. Inserisci solo numeri (es. 12 o 12.99).")
                    input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 

        else:
            print("Nessuna modifica effettuata.")
#richiede come parametro il dizionario del prodotto, il dizionario viene ritornato dalla funzione di ricerca del prodotto
def modificare_o_inserire_nome(prodotto):
    if prodotto == []:
        print("La modifica non può essere effettuata")
        return
    if prodotto["nome"]=="":# se il prodotto = "" dare possibilità di modificarlo -> metodo sopratutto utile quando si mette un nuovo prodotto (vedere codice relativo a input 1)
        # Chiediamo all'utente di inserire la quantità
        nuovo_nome = input(f"Inserisci il nome del prodotto: ")
        prodotto["nome"] = nuovo_nome # modificato il nome
        print(f"Nome inserito: {prodotto["nome"]}")
        input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
        return prodotto
    else:
        # mostriamo il nome attuale e chiediamo se vogliono modificarla
        print(f"Nome del prodotto {prodotto["nome"]}")
        modifica = input("Vuoi modificare il nome? (s/n):") # sulla base dell input utente modifichiamo la quantita 
        if modifica.lower() =="s":
            vecchio_nome = prodotto["nome"]
            nuovo_nome = input(f"Inserisci il nuovo nome del prodotto '{prodotto["nome"]}: ")
            prodotto["nome"]= nuovo_nome
            print(f"Nome del prodotto: '{vecchio_nome}' aggiornato a: '{prodotto["nome"]}")
            input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
        else:
            print("Nessuna modifica effettuata")
            input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 







#richiede come parametro il dizionario del prodotto, il dizionario viene ritornato dalla funzione di ricerca del prodotto
def modifica_o_inserisci_quantita(prodotto):
    if prodotto == []:
        print("La modifica non può essere effettuata")
        return
    if prodotto["quantita"] == 0:# se il prodotto = 0 dare possibilità di modificarlo -> metodo sopratutto utile quando si mette un nuovo prodotto (vedere codice relativo a input 1)
        # Chiediamo all'utente di inserire la quantità
        nuova_quantita = int(input(f"Inserisci la quantità per il prodotto '{prodotto['nome']}': "))
        prodotto['quantita'] = nuova_quantita # modificata la quantita
        print(f"Quantità per '{prodotto['nome']}' inserita: {prodotto['quantita']}")
        input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
        return prodotto
    else:
        # Mostriamo la quantità attuale e chiediamo se vogliono modificarla
        print(f"Quantità attuale di '{prodotto['nome']}': {prodotto["quantita"]}")
        modifica = input("Vuoi modificare la quantità? (s/n): ")
        if modifica.lower() == 's': # sulla base dell input utente modifichiamo la quantita 
            nuova_quantita = int(input(f"Inserisci la nuova quantità per il prodotto '{prodotto['nome']}': "))
            prodotto['quantita'] = nuova_quantita
            print(f"Quantità per '{prodotto['nome']}' aggiornata a: {prodotto['quantita']}")
            input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 

        else:
            print("Nessuna modifica effettuata.")
            input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 

# mostra informazioni
def mostraInfo():
    scelta = input("""
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantita di un prodotto
Invia 4 se vuoi modificare il nome di un  prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l inventario
Invia 7 se vuoi verificare se un prodotto è presente o meno nel magazzino e vedere le sue caratteristiche
Invia 8 se vuoi uscire dal programma (attenzione perderai i dati del magazzino)
>>> """)
    return scelta #ritorna l input dell utente


#   ricercaProdotto
"""
# funzione per verificare la presenza di un prodotto all interno della lista tramite il suo nome
# se - presente stampera tutte le chiavi e valori associate a quell oggetto
quando chiama una funzione diversa da 1, 7, 6 la funzione controlli la presenza o meno del prodotto 
e una volta fatto ritorni il dizionario contenenti gli elementi che l utente vuole modificare, che verrà poi modificato dalle vostre funzioni
# altro - stamperà prodotto non esistente, ritorna false
"""
def ricercaProdotto(listaDizionari, inputUtente, nuovo_dizionario = []):
    if(inputUtente =="2345"):
        return nuovo_dizionario 
    if(inputUtente != "1"):
        nomeProdottoDesiderato = input("Inserisci il nome del prodotto da ricercare: ").lower() 
        for dizionario in listaDizionari:
            if dizionario["nome"] == nomeProdottoDesiderato: # controlla se il valore per la chiave nome di ogni elemento della lista sia uguale a quello selezionato dall utente
                print("Prodotto esistente ")
                for chiave, valore in dizionario.items():#for che andra a stampare tutte le info del prodoyyo
                    print(f"{chiave}: {valore}")
                input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
                if(inputUtente in "2345"):#se l utente ha digitato 2 o 3 o 4 o 5 o 2345 ritorna il dizionario cercato/che vuole modificare l utente
                    
                    return dizionario
                    
                return True #prodotto esistente
        print("Prodotto non esistente")
        input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 

        return [] #prodotto non presente
    else:
        for dizionario in listaDizionari:
            if dizionario["nome"] == "":
                return dizionario

                

def isListaVuota(listaDizionari): #controlla se la lista è vuota
    if len(listaDizionari) == 0:
        print("Magazzino vuoto")
        print("Devi inserire degli elementi dentro al gestionale magazzino se vuoi modificarli o vederli")
        input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
        return True #true se vuota
    else:
        return False#false se presente almeno un elemento

def gestioneMagazzino():
    giacenzeDiMagazzino =[]#la lista dovrebbe essere vuota [], pero l ho riempita per fare delle prove e la funzione 3,7,8 funzionano (in linea purament teorica)
    sceltaUtente = mostraInfo() # chiama funzione mostraInfo che mostra le info e ritorna l inputUtente
    while sceltaUtente != "8":
        if isListaVuota(giacenzeDiMagazzino):
            sceltaUtente ="1" # se lista vuota utente forzato a inserire un nuovo prodotto
        
        #7-8-1
        if (sceltaUtente == "1"):
            print("Inserire un nuovo prodotto")
            giacenzeDiMagazzino.append({"nome":"","codice":"","prezzo":0,"quantita":0})
            dict1 = modificare_o_inserire_nome(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
            sceltaUtente = "2345" #fa si che l input utente sia diverso da 1 e faccia eseguire l if che ritorni il dizionario, al contempo fa si che non vengano chiamate erroneamente le funzioni sotto
            #call funzione 5 codice se valore codice "" allora non stampare vecchio nome ma fare mettere direttamente all utente quello nuovo 
            modifica_o_inserisci_codice(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente, dict1))
            #call funzione 2 prezzo se valore prezzo 0 allora non stampare vecchio nome ma fare mettere direttamente all utente quello nuovo 
            modifica_o_inserisci_prezzo(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente, dict1))
            #call funzione 3 quantita se valore quantita 0  allora non stampare vecchio nome ma fare mettere direttamente all utente quello nuovo
            modifica_o_inserisci_quantita(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente, dict1))# si chiama la funzione modifica_o bla bla che xhiama la funzione ricercaprodotto che ritornera un dizionario
        elif(sceltaUtente == "2"):  
            modifica_o_inserisci_prezzo(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
        
        
        elif(sceltaUtente =="3"):
            modifica_o_inserisci_quantita(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))# si chiama la funzione modifica_o bla bla che xhiama la funzione ricercaprodotto che ritornera un dizionario
                
        elif(sceltaUtente == "4"):
            modificare_o_inserire_nome(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
        elif(sceltaUtente == "5"):
            modifica_o_inserisci_codice(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
        elif(sceltaUtente == "6"):
            mostra_magazzino(giacenzeDiMagazzino)
        elif(sceltaUtente == "7"):
            ricercaProdotto(giacenzeDiMagazzino, sceltaUtente)
                
        elif(sceltaUtente == "8"):
            #si chiude il programma
            print("Programma in chiusura")
            break
    
        sceltaUtente = mostraInfo() # richiediamo l input prima dell inizio del nuovo ciclo 




gestioneMagazzino()
