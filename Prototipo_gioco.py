'''




### **Obiettivo del gioco**
- Il giocatore deve evitare i proiettili sparati dai nemici mentre cerca di sopravvivere il più a lungo possibile.
- Il giocatore può sparare proiettili per eliminare i nemici e accumulare punti.

---

### **Meccaniche principali**
1. **Movimento del giocatore**:
   - Il giocatore può muoversi liberamente su uno schermo 2D.
   
2. **Sparare proiettili**:
   - Il giocatore spara proiettili con un tasto.
   
3. **Nemici che sparano**:
   - I nemici generano continuamente proiettili in schemi complessi.
   
4. **Sopravvivenza e punteggio**:
   - Il punteggio aumenta con il tempo o distruggendo nemici.
   
---

### **Elementi principali**
- **Giocatore**: Un'astronave controllata con la tastiera o il mouse.
- **Nemici**: Generano proiettili con schemi dinamici.
- **Proiettili**:
  - Proiettili del giocatore: Diretti verso i nemici.
  - Proiettili dei nemici

---

## **Prototipo Bullet Hell**

### **Setup del gioco**
'''
import pygame  # Importa il modulo Pygame per creare giochi
import random  # Modulo per generare numeri casuali, utile per spawnare nemici casualmente
import math  # Modulo per operazioni matematiche, non utilizzato direttamente nel codice ma utile per miglioramenti futuri
import logging  # Modulo per la gestione dei log, utile per il debug
import pdb  # Modulo per il debug interattivo (consente di fermare l'esecuzione del programma per l'ispezione)

# Configura il logging, utile per registrare informazioni durante l'esecuzione del gioco
logging.basicConfig(
    filename='game_debug.log',  # Salva i log in un file (puoi rimuovere 'filename' per stamparli in console)
    level=logging.DEBUG,        # Livello minimo dei messaggi da registrare (DEBUG è il più dettagliato)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del messaggio
)

# Inizializza Pygame
pygame.init()

# Costanti del gioco
WIDTH, HEIGHT = 800, 600  # Dimensioni della finestra del gioco
FPS = 60  # Frame per secondo, il gioco aggiornerà il display ogni 1/60 di secondo
PLAYER_SPEED = 5  # Velocità di movimento del giocatore
BULLET_SPEED = 10  # Velocità dei proiettili del giocatore
ENEMY_BULLET_SPEED = 4  # Velocità dei proiettili dei nemici
ENEMY_SPAWN_RATE = 2000  # Millisecondi tra la creazione di un nemico (ogni 2 secondi)
BULLET_COOLDOWN = 300  # Millisecondi tra uno sparo e l'altro del giocatore
score = 0  # Inizializza il punteggio a zero

# Colori utilizzati nel gioco (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Funzione per gestire le collisioni tra proiettili e nemici
def check_collisions():
    global player_bullets, enemies, enemy_bullets, player, score, running

    """Gestione delle collisioni."""
    for bullet in player_bullets:  # Verifica ogni proiettile del giocatore
        hit_enemies = pygame.sprite.spritecollide(bullet, enemies, True)  # Verifica collisione con nemici
        if hit_enemies:
            score += 10  # Aggiungi 10 punti se un nemico viene colpito
            logging.debug(f"Nemico colpito! Punteggio attuale: {score}")
            bullet.kill()  # Rimuove il proiettile dal gioco
            #pdb.set_trace()  # Ferma il gioco per il debug

    # Verifica se i proiettili nemici colpiscono il giocatore
    if pygame.sprite.spritecollide(player, enemy_bullets, True):  # Rimuove i proiettili che colpiscono il giocatore
        print("Game Over")  # Mostra un messaggio di Game Over
        global running
        running = False  # Termina il gioco

# Configura la finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea la finestra di gioco con le dimensioni specificate
pygame.display.set_caption("Bullet Hell")  # Imposta il titolo della finestra
clock = pygame.time.Clock()  # Crea un oggetto per gestire il tempo

# Carica le immagini per il giocatore e il nemico
player_image = pygame.Surface((40, 40))  # Crea una superficie per l'immagine del giocatore
player_image.fill(BLUE)  # Colora l'immagine del giocatore di blu
enemy_image = pygame.Surface((30, 30))  # Crea una superficie per l'immagine del nemico
enemy_image.fill(RED)  # Colora l'immagine del nemico di rosso

# Carica il font per il punteggio
font = pygame.font.SysFont('Arial', 30)  # Font per il punteggio (dimensione 30)

# Classe per il giocatore
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  # L'immagine del giocatore
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))  # Posizione iniziale del giocatore
        self.speed = PLAYER_SPEED  # Velocità di movimento del giocatore
        self.last_shot = pygame.time.get_ticks()  # Tiene traccia dell'ultimo sparo (per il cooldown)

    def update(self, keys):
        # Movimento del giocatore con i tasti freccia
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def shoot(self):
        # Controlla il cooldown prima di sparare
        now = pygame.time.get_ticks()
        if now - self.last_shot >= BULLET_COOLDOWN:  # Se è passato il tempo necessario
            bullet = Bullet(self.rect.centerx, self.rect.top, -BULLET_SPEED, BLUE)  # Crea un nuovo proiettile
            player_bullets.add(bullet)  # Aggiungi il proiettile ai proiettili del giocatore
            all_sprites.add(bullet)  # Aggiungi il proiettile a all_sprites per l'aggiornamento e il rendering
            self.last_shot = now  # Aggiorna il tempo dell'ultimo sparo
            logging.info("Il giocatore ha sparato un proiettile")

# Classe per i proiettili
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, color):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Crea la superficie del proiettile
        self.image.fill(color)  # Colora il proiettile con il colore passato
        self.rect = self.image.get_rect(center=(x, y))  # Posiziona il proiettile
        self.speed = speed  # Imposta la velocità del proiettile

    def update(self):
        self.rect.y += self.speed  # Muove il proiettile lungo l'asse Y
        # Rimuove il proiettile se esce dallo schermo
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

# Classe per i nemici
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image  # L'immagine del nemico
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2)))  # Posizione casuale
        self.last_shot = pygame.time.get_ticks()  # Tiene traccia dell'ultimo sparo (per il cooldown)

    def update(self):
        # I nemici sparano proiettili a intervalli regolari
        now = pygame.time.get_ticks()
        if now - self.last_shot > 1000:  # I nemici sparano ogni secondo
            bullet = Bullet(self.rect.centerx, self.rect.bottom, ENEMY_BULLET_SPEED, RED)  # Crea un proiettile nemico
            enemy_bullets.add(bullet)  # Aggiungi il proiettile ai proiettili dei nemici
            all_sprites.add(bullet)  # Aggiungi il proiettile a all_sprites
            self.last_shot = now  # Aggiorna il tempo dell'ultimo sparo

# Gruppi di sprite (oggetti del gioco)
all_sprites = pygame.sprite.Group()  # Tutti gli oggetti (giocatore, nemici, proiettili)
player_bullets = pygame.sprite.Group()  # Proiettili del giocatore
enemy_bullets = pygame.sprite.Group()  # Proiettili dei nemici
enemies = pygame.sprite.Group()  # Nemici

# Crea l'oggetto giocatore e aggiungilo ai gruppi
player = Player()
all_sprites.add(player)

# Imposta un timer per spawnare i nemici a intervalli regolari
pygame.time.set_timer(pygame.USEREVENT, ENEMY_SPAWN_RATE)

# Variabili di stato
score = 0
running = True  # Indica se il gioco è in esecuzione

# Ciclo principale del gioco
while running:
    # Gestione degli eventi (es. chiusura del gioco)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Se l'utente chiude la finestra, termina il gioco
        elif event.type == pygame.USEREVENT:  # Se è passato il timer, spawn un nemico
            enemy = Enemy()  # Crea un nuovo nemico
            all_sprites.add(enemy)  # Aggiungi il nemico a all_sprites
            enemies.add(enemy)  # Aggiungi il nemico ai nemici

    # Gestione dell'input da tastiera (movimento e sparo)
    keys = pygame.key.get_pressed()

    # Aggiorna la posizione del giocatore
    player.update(keys)

    # Sparo del giocatore se viene premuto il tasto spazio
    if keys[pygame.K_SPACE]:
        player.shoot()

    # Aggiorna tutti gli altri sprite (tranne il giocatore)
    for sprite in all_sprites:
        if not isinstance(sprite, Player):  # Escludi il giocatore dalla lista
            sprite.update()

    # Controllo delle collisioni
    check_collisions()

    # Disegna tutto (sfondo, oggetti, etc.)
    screen.fill(WHITE)  # Riempi lo schermo con il colore bianco
    all_sprites.draw(screen)  # Disegna tutti gli sprite

    # Disegna il punteggio
    score_text = font.render(f"Punteggio: {score}", True, BLACK)  # Crea una superficie con il testo del punteggio
    screen.blit(score_text, (10, 10))  # Disegna il punteggio in alto a sinistra

    pygame.display.flip()  # Aggiorna lo schermo
    clock.tick(FPS)  # Limita il numero di frame al secondo

pygame.quit()  # Termina Pygame




## **Spiegazione del codice**
'''
1. **Player e movimento**: Il giocatore può muoversi in ogni direzione e sparare proiettili, 
     con un cooldown per evitare spam.
2. **Nemici**: I nemici sparano proiettili casuali a intervalli regolari.
3. **Collisioni**:
   - Proiettili del giocatore eliminano i nemici.
   - Proiettili nemici causano il **Game Over**.
4. **Punteggio**: Aumenta con l'eliminazione dei nemici.


'''