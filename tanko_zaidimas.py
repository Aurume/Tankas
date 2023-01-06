import math
import random

import pygame

pygame.init()  # turi būti iškart po importų prieš viską
clock = pygame.time.Clock()

visas_langas = pygame.display.set_mode((800, 600))  # lango plotis, aukštis
pygame.display.set_caption('Tankiukai')  # mano lango pavadinimas

ikona = pygame.image.load("tankiukas1.png")
pygame.display.set_icon(ikona)  # kad pakeisti ikonėlę i tanko ikoną

# Tankas
tanko_figura = pygame.image.load("melynas_tankas.png")
x = 470  # koordinatė x, kur pradžioj atsiras mano tankas. darau daugmaž per vidurį.
y = 550  # koordinatė y ašies,  kiek į apačią bus tankas
tanko_pokytis = 0

# Priešas
prieso_pav = []
prieso_x = []
prieso_y = []
priesas_x_kinta = []
priesas_y_kinta = []
kiek_priesu = 5

for priesas_pirminis in range(kiek_priesu):
    prieso_pav.append(pygame.image.load('moliugas.png'))  # pridedu priešus i tuščią masyvą
    prieso_x.append(random.randint(0, 800))  # priešo atsiradimo x koordinatės
    prieso_y.append(random.randint(50, 150))  # priešo y
    priesas_x_kinta.append(4)  # kiek juda x ašimi kai priliečia kraštą
    priesas_y_kinta.append(20)  # kai atsitrenks į sieną, kiek žemyn judės

# Kulkos
kulkos_figura = pygame.image.load('kulka.png')
kulkos_x = 0  # nereikia nustatyti, nes x pasiima tanko kaip pradinį
kulkos_y = 480  # kokiam aukštį
kulkos_x_pokytis = 0
kulkos_y_pokytis = 10  # greitis
kulkos_busena = "pasiruoses"  #kulka nematoma, kol būsena tokia

# Taškai
tasku_kiekis = 0
font = pygame.font.Font('freesansbold.ttf', 22)
# kairiam kampe, viršuje bus taškai:
teksto_x = 10
teksto_y = 10

# Žaidimo pabaiga
pabaiga = pygame.font.Font('freesansbold.ttf', 30)
pabaiga2 = pygame.font.Font('freesansbold.ttf', 30)


# Skaičiuojam taškus
def rodyti_taskus(x, y):
    taskai = font.render("Taškai: " + str(tasku_kiekis), True, (0, 0, 0))
    visas_langas.blit(taskai, (x, y))


def pabaigos_tekstas():
    teksto_pab = pabaiga.render("Priešas sunaikino tanką!", True, (0, 0, 0)) # užrašas, kuris pasirodo, kai moliūgas paliečia tanką.
    teksto_pab1 = pabaiga2.render("ŽAIDIMO PABAIGA!", True, (0, 0, 0))
    visas_langas.blit(teksto_pab, (220, 240))
    visas_langas.blit(teksto_pab1, (260, 280))

# Žaidėjas
def tankas(x, y):
    visas_langas.blit(tanko_figura, (x, y))


def priesas(x, y, priesas_pagr):
    visas_langas.blit(prieso_pav[priesas_pagr], (x, y))


def saudyti(x, y):
    global kulkos_busena
    kulkos_busena = "saudau"
    visas_langas.blit(kulkos_figura, (x + 25, y + 10))  # kad atsirastų tanko centre(x - puse mano tanko) ir šiek tiek virš tanko(y)


# skaičiuojam  vidurio taško atstumą tarp kulkos ir tanko, naudojant determinantą.
def susidurimas(prieso_x, prieso_y, kulkos_x, kulkos_y):
    atstumas = math.sqrt(math.pow(prieso_x - kulkos_x, 2) + (math.pow(prieso_y - kulkos_y, 2)))
    if atstumas < 15:  # koks atstumas pikseliais tarp abiejų, kad patikrinti kada susiduria
        return True
    else:
        return False


veikia = True
while veikia:  # main game loop

    visas_langas.fill((255, 255, 255))  # balta
    for event in pygame.event.get():
        # visas_langas.fill((255, 255, 255))  # butina tuple masyvas, kitu atveju neveiks
        if event.type == pygame.QUIT:  # tikrina ar yra veiksmas išeiti
            veikia = False

        # kas_paspausta = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:  # tikrinam ar nuspausti mygtukai
            if event.key == pygame.K_LEFT:
                tanko_pokytis = -5
            if event.key == pygame.K_RIGHT:
                tanko_pokytis = 5
            if event.key == pygame.K_SPACE:
                if kulkos_busena == "pasiruoses":  # kad butu galima šaudyti tik kai nebėra kulkos ekrane
                    kulkos_x = x  # išsaugau naują reikšmę, kad kulka nesektų paskui kai juda tankas
                    saudyti(kulkos_x, kulkos_y)

        if event.type == pygame.KEYUP:  # jeigu niekas nenuspausta
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                tanko_pokytis = 0

    x += tanko_pokytis
    if x <= 0:  # patikrinu ar x nemažiau už nulį tam, kad neišeitų tankas uz ribų kairėje
        x = 0
    elif x >= 750:  # kiek maks į dešinę (atimu iš visos x ašies savo tanko dydi - 50)
        x = 750


    for priesas_pirminis in range(kiek_priesu):

        # žaidimas baigtas
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

            prieso_x[priesas_pirminis] = random.randint(0, 749)  # ne daugiau 750
            prieso_y[priesas_pirminis] = random.randint(50, 150)  # 50, 150

        priesas(prieso_x[priesas_pirminis], prieso_y[priesas_pirminis], priesas_pirminis)

    # kaip judes kulkos
    if kulkos_y <= 0:  # jei pasieks viršų ties nuline riba-nusiresetins ir vel bus pradinėje padėtyje
        kulkos_y = 480  # kad grįžtų į pradinę padėtį
        kulkos_busena = "pasiruoses"

    if kulkos_busena == "saudau":
        saudyti(kulkos_x, kulkos_y)
        kulkos_y -= kulkos_y_pokytis

    # visas_langas.fill((255, 255, 255)) #atnaujinam langą, kad kaskart nebūtų tempiamas paveikslėlio vaizdas judant
    tankas(x, y)

    # priesas(prieso_x, prieso_y)
    rodyti_taskus(teksto_x, teksto_y)

    pygame.display.update()
    clock.tick(90) # kokiu greičiu laksto tankas ir kulkos

# pygame.quit()  # išėjimo funkcija
