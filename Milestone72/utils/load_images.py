import pygame
import os
from numpy import empty
from random import randint
import utils.setup as sp



# load images: spacecrafts, asteroids, background, explosion
def load_imag(): 
    
    N_spcft = 5
    N_aster = 7
    N_bg = 14

    spcft = empty([N_spcft], dtype=pygame.Surface)
    aster = empty([N_aster], dtype=pygame.Surface)
    bg = empty([N_bg], dtype=pygame.Surface)

    spcft[0] = pygame.transform.scale(pygame.image.load(os.path.join("doc/images/spacecraft/iss.png")), (sp.SPCRFT_W0,sp.SPCRFT_H0))
    spcft[1] = pygame.transform.scale(pygame.image.load(os.path.join("doc/images/spacecraft/soyuz.png")), (sp.SPCRFT_W0,sp.SPCRFT_H0))
    spcft[2] = pygame.transform.scale(pygame.image.load(os.path.join("doc/images/spacecraft/space_shuttle.png")), (sp.SPCRFT_W0,sp.SPCRFT_H0))
    spcft[3] = pygame.transform.scale(pygame.image.load(os.path.join("doc/images/spacecraft/spaceX_dragon.png")), (sp.SPCRFT_W0,sp.SPCRFT_H0))
    spcft[4] = pygame.transform.scale(pygame.image.load(os.path.join("doc/images/spacecraft/starman.png")), (sp.SPCRFT_W0,sp.SPCRFT_H0))

    aster[0] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_1.png"))
    aster[1] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_2.png"))
    aster[2] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_3.png"))
    aster[3] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_4.png"))
    aster[4] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_5.png"))
    aster[5] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_6.png"))
    aster[6] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_7.png"))

    bg[0]  = pygame.image.load(os.path.join("doc/images/background/bg_1.jpg"))
    bg[1]  = pygame.image.load(os.path.join("doc/images/background/bg_2.jpg"))
    bg[2]  = pygame.image.load(os.path.join("doc/images/background/bg_3.jpg"))
    bg[3]  = pygame.image.load(os.path.join("doc/images/background/bg_4.jpg"))
    bg[4]  = pygame.image.load(os.path.join("doc/images/background/bg_5.jpg"))
    bg[5]  = pygame.image.load(os.path.join("doc/images/background/bg_6.jpg"))
    bg[6]  = pygame.image.load(os.path.join("doc/images/background/bg_7.jpg"))
    bg[7]  = pygame.image.load(os.path.join("doc/images/background/bg_8.jpg"))
    bg[8]  = pygame.image.load(os.path.join("doc/images/background/bg_9.jpg"))
    bg[9]  = pygame.image.load(os.path.join("doc/images/background/bg_10.jpg"))
    bg[10]  = pygame.image.load(os.path.join("doc/images/background/bg_11.jpg"))
    bg[11]  = pygame.image.load(os.path.join("doc/images/background/bg_12.jpg"))
    bg[12]  = pygame.image.load(os.path.join("doc/images/background/bg_13.jpg"))
    bg[13]  = pygame.image.load(os.path.join("doc/images/background/bg_14.jpg"))

    exp = pygame.image.load(os.path.join("doc/images/spacecraft/explosion.png"))


    #only return one spacecraft and one backgoround
    a = randint(0, N_spcft-1)
    b = randint(0, N_bg-1)

    return spcft[a], aster, bg[b], exp


