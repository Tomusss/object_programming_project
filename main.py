import pygame
import random

pygame.init()
pygame.font.init()

Banan_img = pygame.image.load('banan.png')
Jabłko_img = pygame.image.load('jabłko.png')
Truskawka_img = pygame.image.load('truskawka.png')
Cytryna_img = pygame.image.load('cytryna.png')
Czereśnia_img = pygame.image.load('czereśnia.png')
Gruszka_img = pygame.image.load('gruszka.png')
Arbuz_img = pygame.image.load('arbuz.png')
Winogrona_img = pygame.image.load('winogrona.png')
Bomba_img = pygame.image.load('bomba.png')
Skrzynka_img = pygame.image.load('skrzynka.png')

# Ustawienia ekranu
SZEROKOSC = 800
WYSOKOSC = 600

# Ekran
screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))

pygame.display.set_caption('Owocowy zbiór')

# muzyka
pygame.mixer.init()
pygame.mixer.music.load('bff-instrumental.mp3') 
pygame.mixer.music.play(-1)

class Owoce(pygame.sprite.Sprite):
    """
    Klasa reprezentująca spadające owoce.
    """
    mnoznik = 1.1
    zdjecia_owocow = ['banan.png', 'jabłko.png', 'truskawka.png', 'cytryna.png', 'czereśnia.png', 'winogrona.png', 'arbuz.png','gruszka.png' ]
    def __init__(self, szerokosc_ekranu: int, wysokosc_ekranu: int) -> None:
        """
        Inicjalizuje owoc na ekranie o podanej szerokości i wysokości.
        """
        super().__init__()
        zdjecia_owocow = random.choice(Owoce.zdjecia_owocow)  # Losowy wybór obrazu owocu
        self.image = pygame.image.load(zdjecia_owocow).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, szerokosc_ekranu - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randrange(2, 4)/3
        self.wysokosc_ekranu = wysokosc_ekranu

    def update(self) -> None:
        """
        Aktualizuje pozycję owocu na ekranie.
        """
        self.rect.y += (1+self.speed)*Owoce.mnoznik
        if self.rect.top -10 > self.wysokosc_ekranu:
            self.kill()

class Bomby(Owoce):
    """
    Klasa reprezentująca bomby, które również spadają jak owoce.
    """
    def __init__(self, szerokosc_ekranu: int, wysokosc_ekranu: int) -> None:
        """
        Inicjalizuje bombę na ekranie o podanej szerokości i wysokości.
        """
        super().__init__(szerokosc_ekranu, wysokosc_ekranu)
        self.image = pygame.image.load('bomba.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 65))

    def update(self) -> None:
        """
        Aktualizuje pozycję bomby na ekranie.
        """
        super().update()

class Gracz(pygame.sprite.Sprite):
    """
    Klasa reprezentująca gracza, który porusza się po ekranie.
    """
    def __init__(self, szerokosc_ekranu: int, wysokosc_ekranu: int) -> None:
        """
        Inicjalizuje gracza na ekranie o podanej szerokości i wysokości.
        """
        super().__init__()
        self.image = pygame.image.load('skrzynka.png').convert_alpha() 
        self.image = pygame.transform.scale(self.image, (140, 65))
        self.rect = self.image.get_rect()
        self.rect.x = szerokosc_ekranu/2
        self.rect.y = wysokosc_ekranu - self.rect.height
        self.predkosc = 6

    def update(self) -> None:
        """
        Aktualizuje pozycję gracza na ekranie na podstawie wciśniętych klawiszy.
        """        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.predkosc
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.predkosc

        if self.rect.x > SZEROKOSC-self.rect.width:
            self.rect.x = SZEROKOSC-self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
# zmiana glosnosci muzyki w trakcie gry i w menu       
def glosnosc_menu() -> None:
    """
    Ustawia głośność muzyki w menu na 10%.
    """
    pygame.mixer.music.set_volume(0.1)

def glosnosc_gry() -> None:
    """
    Ustawia głośność muzyki gry na 50%.
    """
    pygame.mixer.music.set_volume(0.5)

def Pauza() -> None:
    """
    Wyświetla ekran pauzy.
    """
    przyciemnienie = pygame.Surface((SZEROKOSC, WYSOKOSC))
    przyciemnienie.set_alpha(150)

    font = pygame.font.Font(None, 72)
    pauza_tekst = font.render("PAUZA", True, 'white')
    pauza_tekst_rect = pauza_tekst.get_rect(center=(SZEROKOSC // 2, WYSOKOSC // 2))
    
    screen.blit(przyciemnienie, (0, 0))
    screen.blit(pauza_tekst, pauza_tekst_rect)

# Ekran startowy
def EkranStartowy() -> None:
    """
    Wyświetla ekran startowy gry.
    """
    tlo = pygame.image.load('tlo.png')
    tlo = pygame.transform.scale(tlo, (SZEROKOSC, WYSOKOSC))
    
    tytul_font = pygame.font.Font(None, 100)
    tytul_tekst = tytul_font.render("Owocowy zbiór", True, 'black')
    tytul_tekst_rect = tytul_tekst.get_rect(center=(SZEROKOSC // 2, WYSOKOSC // 2 + 200 ))

    font = pygame.font.Font(None, 50)
    start_tekst = font.render("ZACZNIJ GRĘ", True, 'white')
    start_tekst_rect = start_tekst.get_rect(center=(SZEROKOSC // 2, WYSOKOSC // 2 + 100))

    start_button = pygame.Rect(SZEROKOSC // 2 - 150, WYSOKOSC // 2 + 50, 300, 100)

    screen.blit(tlo, (0, 0))
    screen.blit(tytul_tekst, tytul_tekst_rect)
    pygame.draw.rect(screen, 'black', start_button)
    screen.blit(start_tekst, start_tekst_rect)
    pygame.display.update()

    glosnosc_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    glosnosc_gry()
                    return



def EkranKoncowy(wynik: int) -> str:
    """
    Wyświetla ekran końcowy z wynikiem.
    """

    przyciemnienie = pygame.Surface((SZEROKOSC, WYSOKOSC))
    przyciemnienie.set_alpha(150)

    tlo = pygame.Surface((SZEROKOSC*0.65,WYSOKOSC*0.65))
    tlo.fill('white')
    tlo_rect = tlo.get_rect(center=(SZEROKOSC // 2, WYSOKOSC // 2))

    font = pygame.font.Font(None, 72)
    font2 = pygame.font.Font(None, 50)
    koniec_tekst = font.render('PRZEGRAŁEŚ', True, 'blue')
    wynik_tekst = font2.render(f"Twój wynik: {wynik}", True, 'grey')
    wynik_tekst_rect = wynik_tekst.get_rect(center=(SZEROKOSC//2, WYSOKOSC//2 - 90))
    koniec_tekst_rect = koniec_tekst.get_rect(center=(SZEROKOSC // 2, WYSOKOSC//2 - 150))

    menu_button = pygame.Rect(SZEROKOSC // 2 - 150, WYSOKOSC // 2, 300, 50)
    restart_button = pygame.Rect(SZEROKOSC // 2 - 150, WYSOKOSC // 2 + 100, 300, 50)

    menu_tekst = font2.render("Przejdź do menu", True, 'white')
    restart_tekst = font2.render("Zacznij od nowa", True, 'white')
    menu_tekst_rect = menu_tekst.get_rect(center=(menu_button.center))
    restart_tekst_rect = restart_tekst.get_rect(center=(restart_button.center))

    screen.blit(przyciemnienie, (0, 0))
    screen.blit(tlo, tlo_rect)
    screen.blit(wynik_tekst, wynik_tekst_rect)
    screen.blit(koniec_tekst, koniec_tekst_rect)
    pygame.draw.rect(screen, 'black', menu_button)
    pygame.draw.rect(screen, 'black', restart_button)
    screen.blit(menu_tekst, menu_tekst_rect)
    screen.blit(restart_tekst, restart_tekst_rect)
    pygame.display.update()

    glosnosc_menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    EkranStartowy()
                    return "menu"
                if restart_button.collidepoint(event.pos):
                    glosnosc_gry()
                    return "restart"

def resetuj_rozgrywke() -> None:
    """
    Resetuje ustawienia gry.
    """
    global owoce, bomby, gracz, wynik, zycia, max_owocow, max_bomb, szansa_owocow, szansa_bomb, poziom, pauza
    owoce = pygame.sprite.Group()
    bomby = pygame.sprite.Group()
    gracz = pygame.sprite.GroupSingle(Gracz(SZEROKOSC, WYSOKOSC))
    wynik = 0
    zycia = 3
    max_owocow = 3
    max_bomb = 1
    szansa_owocow = 0.007
    szansa_bomb = 0.002
    poziom = 1
    pauza = False

# Ustawienia gry
FPS = 60
dziala = True
zegar = pygame.time.Clock()

owoce = pygame.sprite.Group()
bomby = pygame.sprite.Group()
gracz = pygame.sprite.GroupSingle(Gracz(SZEROKOSC, WYSOKOSC))
wynik = 0
zycia = 3
max_owocow = 3
max_bomb = 1
szansa_owocow = 0.007
szansa_bomb = 0.002
poziom = 1
pauza = False

# Wyświetl ekran startowy
EkranStartowy()

# Główna pętla gry
while dziala:
    # Zamykanie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pauza = not pauza
    

    # Dodawanie nowych owoców
    if len(owoce) < max_owocow:
        if random.random() < szansa_owocow:
            nowy_owoc = Owoce(SZEROKOSC, WYSOKOSC)
            owoce.add(nowy_owoc)
    if len(bomby) < max_bomb:
        if random.random() < szansa_bomb:
            bomby.add(Bomby(SZEROKOSC, WYSOKOSC))

    # Kolizje
    kolizje_owoce = pygame.sprite.spritecollide(gracz.sprite,owoce,True)
    for kolizja in kolizje_owoce:
        wynik += 1
        if wynik%5== 0:
            poziom = wynik//10
            szansa_bomb += 0.0005
            szansa_owocow += 0.0001
            Owoce.mnoznik += 0.1
            poziom += 1
        if wynik%10 == 0:
            max_owocow += 1
            max_bomb += 1

    if pygame.sprite.spritecollide(gracz.sprite,bomby,False):
        dziala = False
    for owoc in owoce:
        if owoc.rect.top > WYSOKOSC:
            owoc.kill()
            zycia -=1
            if zycia <= 0:
                dziala = False

    # Aktualizacja
    if not pauza:
        owoce.update()
        bomby.update()
        gracz.update()
    


    # Rysowanie
    screen.fill('lightblue')
    owoce.draw(screen)
    bomby.draw(screen)
    gracz.draw(screen)

    # Wynik zycia i level
    font = pygame.font.Font(None, 20)
    wynik_text = font.render(f'Wynik: {wynik}', True, 'black')
    zycia_text = font.render(F'Życia: {zycia}', True, 'red')
    poziom_text = font.render(F'Poziom: {poziom}', True, 'blue')
    screen.blit(wynik_text, (10, 10))
    screen.blit(zycia_text,(10,30))
    screen.blit(poziom_text,(10,50))
    
    # Włączanie pauzy
    if pauza:
        Pauza()

    # Sterowanie ekranem końcowym
    if dziala == False:
        wynik_ekranu = EkranKoncowy(wynik)
        if wynik_ekranu == "restart":
            resetuj_rozgrywke()
            dziala = True
        elif wynik_ekranu == "menu":
            EkranStartowy()
            resetuj_rozgrywke()
            dziala = True
    

    pygame.display.update()

    # FPS
    zegar.tick(FPS)

pygame.quit()