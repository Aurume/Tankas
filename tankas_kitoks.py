import pygame
from pygame.locals import *

pygame.init()  # turi buti iskart po importu pries viska
clock = pygame.time.Clock()

visas_langas = pygame.display.set_mode((600, 600))  # lango plotis, aukstis
pygame.display.set_caption('Tankiukai')  # mano lango pavadinimas

ikona = pygame.image.load("tankiukas1.png")
pygame.display.set_icon(ikona)  # kad pakeisti ikonele i tanka

x, y = 0, 550  # koordinates kur bus tankas
tanko_figura = pygame.image.load("melynas_tankas.png")

veikia = True
while veikia:  # main game loop
    visas_langas.blit(tanko_figura, (x, y))
    for event in pygame.event.get():
        visas_langas.fill((255, 255, 255))  # butina tuple masyvas, kitu atveju neveiks
        if event.type == QUIT:  # tikrina ar veiksmas yra iseiti
            veikia = False


    kas_paspausta = pygame.key.get_pressed()
    if kas_paspausta[pygame.K_LEFT]:
        x -= 1
    if kas_paspausta[pygame.K_RIGHT]:
        x += 1
    if kas_paspausta[pygame.K_UP]:
        y -= 1
    if kas_paspausta[pygame.K_DOWN]:
        y += 1


    #visas_langas.fill((0, 0, 0)) #atnaujinam langa, kad kaskart nevilktu paveikslelio vaizdo

    pygame.display.update()
    clock.tick(120)

pygame.quit()  # isejimo funkcija
