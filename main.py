import pygame
from pygame.locals import *

pygame.init()  # turi buti iskart po importu pries viska

visas_langas = pygame.display.set_mode((600, 600))  # lango plotis, aukstis
pygame.display.set_caption('Tankiukai')  # mano lango pavadinimas

ikona = pygame.image.load("tankiukas1.png")
pygame.display.set_icon(ikona)  # kad pakeisti ikonele i tanka

clock = pygame.time.Clock()
tanko_figura = pygame.image.load("mini_tankas.png")


def tankas(x, y):
    visas_langas.blit(tanko_figura, (x, y))


# tankas ir jo greitis(kiek pajuda vienu paspaudimu)
x = 50
y = 50
plotis = 80
aukstis = 40
tempas = 5


# tanko_figura = pygame.image.load("kitoks_tankas.png")
# tanko_figura.get_rect(x, y )

veikia = True
while veikia:  # main game loop
    visas_langas.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:  # tikrina ar veiksmas yra iseiti
            veikia = False

    kas_paspausta = pygame.key.get_pressed()
    if kas_paspausta[pygame.K_LEFT] and x > tempas: # Vakarai/ ir apriboju kad negaletu iseiti uz ribu
        x -= tempas                  # kad judeti x asimi i kaire, turiu atimti
    if kas_paspausta[pygame.K_RIGHT] and x < 600 - plotis: # Rytai/ atimu is ekrano plocio savo ploti, kad neiseitu uz ribu i desine
        x += tempas
    if kas_paspausta[pygame.K_UP] and y > tempas: # Siaure
        y -= tempas
    if kas_paspausta[pygame.K_DOWN] and y < 600 - aukstis - tempas: # Pietus
        y += tempas

    # mini_tankas = pygame.transform.scale(tanko_figura, (x, y))
    # visas_langas.blit(mini_tankas, (80, 80))

    # visas_langas.blit(mini_tankas, (mini_tankas.x, mini_tankas.y))
    # pygame.draw.rect(visas_langas, (0, 255, 155), (x, y, plotis, aukstis)) #piesiu tanko figura, staciakampi


    #visas_langas.fill(0, 0, 0)
    tankas(x, y)

    pygame.display.update()
    clock.tick(30)

pygame.quit()  # isejimo funkcija
