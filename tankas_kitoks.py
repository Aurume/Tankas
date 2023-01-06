import math
import random

import pygame

pygame.init()  # turi buti iskart po importu pries viska
clock = pygame.time.Clock()

visas_langas = pygame.display.set_mode((800, 600))  # lango plotis, aukstis
pygame.display.set_caption('Tankiukai')  # mano lango pavadinimas

ikona = pygame.image.load("tankiukas1.png")
pygame.display.set_icon(ikona)  # kad pakeisti ikonele i tanko ikona

# pats tankas

tanko_figura = pygame.image.load("melynas_tankas.png")
x = 470  # koordinate x, kur pradzioj atsiras mano tankas. darau daugmaz per viduri.
y = 550  # koordinate y asies,  kiek i apacia bus tankas
tanko_pokytis = 0

# priešai
prieso_pav = []
prieso_x = []
prieso_y = []
priesas_x_kinta = []
priesas_y_kinta = []
kiek_priesu = 6

for priesas_pirminis in range(kiek_priesu):
    prieso_pav.append(pygame.image.load('moliugas.png'))  # pridedu priesus i tuscia masyva
    prieso_x.append(random.randint(0, 750))  # didesnis skaicius, daugiau tasku
    prieso_y.append(random.randint(50, 150))
    priesas_x_kinta.append(4)  # jeigu nulis-taikinys nejuda
    priesas_y_kinta.append(40)

# Kulkos

kulkos_figura = pygame.image.load('kulka.png')
kulkos_x = 0
kulkos_y = 480
kulkos_x_pokytis = 0
kulkos_y_pokytis = 10
kulkos_busena = "pasiruoses"

# taskai

tasku_kiekis = 0
font = pygame.font.Font('freesansbold.ttf', 22)

teksto_x = 10
teksto_y = 10

# Zaidimo pabaiga
pabaiga = pygame.font.Font('freesansbold.ttf', 34)


# skaicuoti taskus
def rodyti_taskus(x, y):
    taskai = font.render("Taškai: " + str(tasku_kiekis), True, (0, 0, 0))
    visas_langas.blit(taskai, (x, y))


def pabaigos_tekstas():
    teksto_pab = pabaiga.render("PABAIGA!", True, (0, 0, 0))
    visas_langas.blit(teksto_pab, (270, 250))


# zaidejas
def tankas(x, y):
    visas_langas.blit(tanko_figura, (x, y))


def priesas(x, y, priesas_pagr):
    visas_langas.blit(prieso_pav[priesas_pagr], (x, y))


def saudyti(x, y):
    global kulkos_busena
    kulkos_busena = "saudau"
    visas_langas.blit(kulkos_figura, (x + 16, y + 10))  # pasigilinti ka daro skaiciai.x+16/y+10


# skaiciuojam  vidurio tasko atstuma tarp kulkos ir tanko, naudojant determinanta.
def susidurimas(prieso_x, prieso_y, kulkos_x, kulkos_y):
    atstumas = math.sqrt(math.pow(prieso_x - kulkos_x, 2) + (math.pow(prieso_y - kulkos_y, 2)))
    if atstumas < 27:  # koks atstumas pikseliais tarp abieju, kad patikrinti kada susiduria
        return True
    else:
        return False


veikia = True
while veikia:  # main game loop
    # clock.tick(60)
    visas_langas.fill((255, 255, 255))  # balta
    for event in pygame.event.get():
        # visas_langas.fill((255, 255, 255))  # butina tuple masyvas, kitu atveju neveiks
        if event.type == pygame.QUIT:  # tikrina ar veiksmas yra iseiti
            veikia = False

        # kas_paspausta = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:  # tikrinam ar nuspausti mygtukai
            if event.key == pygame.K_LEFT:
                tanko_pokytis = -5
            if event.key == pygame.K_RIGHT:
                tanko_pokytis = 5
            if event.key == pygame.K_SPACE:
                if kulkos_busena == "pasiruoses":  # kad butu galima saudyt tik kai nebera ekrane
                    kulkos_x = x  # issaugau nauja reiksme, kad kulka nesektu tanko
                    saudyti(kulkos_x, kulkos_y)

        if event.type == pygame.KEYUP:  # jeigu niekas nenuspausta
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                tanko_pokytis = 0

    x += tanko_pokytis
    if x <= 0:  # kaire puse.patikrinu ar x nemaziau uz nuli, tam kad neiseitu tankas uz ribu
        x = 0
    elif x >= 750:  # kiek maks i desine(atimu is viso x asies savo tanko dydi - 50)
        x = 750

    for priesas_pirminis in range(kiek_priesu):

        # pabaiga zaidimo
        if prieso_y[priesas_pirminis] > 440:
            for priesas_kitas in range(kiek_priesu):
                prieso_y[priesas_kitas] = 2000
            pabaigos_tekstas()
            break

        prieso_x[priesas_pirminis] += priesas_x_kinta[priesas_pirminis]
        if prieso_x[priesas_pirminis] <= 0:
            priesas_x_kinta[priesas_pirminis] = 4
            priesas_y_kinta[priesas_pirminis] += priesas_y_kinta[priesas_pirminis]
        elif prieso_x[priesas_pirminis] >= 740:
            priesas_x_kinta[priesas_pirminis] = -4
            prieso_y[priesas_pirminis] += priesas_y_kinta[priesas_pirminis]

        # susidurimas tanko ir kulkos
        susidure = susidurimas(prieso_x[priesas_pirminis], prieso_y[priesas_pirminis], kulkos_x, kulkos_y)
        if susidure:
            kulkos_y = 480  # pradine padetis
            kulkos_busena = "pasiruoses"
            tasku_kiekis += 1

            prieso_x[priesas_pirminis] = random.randint(0, 749)  # 0, 749
            prieso_y[priesas_pirminis] = random.randint(50, 150)  # 50, 150

        priesas(prieso_x[priesas_pirminis], prieso_y[priesas_pirminis], priesas_pirminis)

    # kaip judes kulkos
    if kulkos_y <= 0:  # jei pasieks virsu ties nuline riba-nusiresetins ir vel bus pradinej padetyje
        kulkos_y = 480  # grista i pradine padeti
        kulkos_busena = "pasiruoses"

    if kulkos_busena == "saudau":
        saudyti(kulkos_x, kulkos_y)
        kulkos_y -= kulkos_y_pokytis

    # visas_langas.fill((255, 255, 255)) #atnaujinam langa, kad kaskart nebutu tempiamas paveikslelio vaizdas judant
    tankas(x, y)

    # priesas(prieso_x, prieso_y)
    rodyti_taskus(teksto_x, teksto_y)

    pygame.display.update()
    clock.tick(90) # kokiu greiciu laksto tankas ir kulkos

# pygame.quit()  # isejimo funkcija
