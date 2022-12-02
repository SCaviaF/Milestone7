
import os
import pickle
import random
import time
import pyautogui

import test_alpha.test_alpha1 as talpha

from numpy import cos, zeros, mean

import neat
import pygame
import visualize
pygame.font.init()  # init font


def main(cap, hands, mp_hands, mp_drawing_styles, mp_drawing):
    WIN_WIDTH = 1500
    WIN_HEIGHT = 800
    #STAT_FONT = pygame.font.SysFont("comicsans", 50)
    #END_FONT = pygame.font.SysFont("comicsans", 70)
    DRAW_LINES = False

    Bird_Width = 50
    Bird_Height = 35

    bird_img = [pygame.transform.scale(pygame.image.load(os.path.join("pictures", "pic_1.png")), (Bird_Width, Bird_Height) )]
    bird_img1 = [pygame.transform.scale(pygame.image.load(os.path.join("pictures", "pic_1.png")), (Bird_Width, Bird_Height) )]
    pipe_img  = pygame.transform.scale2x(pygame.image.load(os.path.join("pictures", "pic_4.png")))
    base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("pictures", "pic_3.png")))
    bg_img  = pygame.transform.scale(pygame.image.load(os.path.join("pictures", "pic_2.png")), (WIN_WIDTH, WIN_HEIGHT))


    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    class Bird:
        IMGS = bird_img

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.tilt = 0  # degrees to tilt
            self.tick_count = 0
            self.vel = 0
            self.height = self.y
            self.img_count = 0
            self.img = bird_img

        def draw(self, win):
            win.blit(bird_img[0], (self.x, self.y))

        def get_mask(self):
            return pygame.mask.from_surface(self.img)



    #window
    def draw_window(win, bird):
        win.blit(bg_img, (0,0))
        bird.draw(win)

        pygame.display.update()


    #loop game
    x, y, z = talpha.test_3(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)
    # define the number of past values to use in the moving average
    N = 20
    # initialize a list to store the past values
    past_values = []
    weighted_avg_denominator = sum(range(1, N+1))

    while True:

        # retrieve the current position of the bird
        x, y, z = talpha.test_3(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)
        # update the list of past values
        past_values.append((x, y, z))
        # remove the oldest value from the list if the list is longer than N
        if len(past_values) > N:
            past_values.pop(0)
        # compute the weighted average of the current and past positions
        # to get the smoothed position of the bird
        x_smooth = sum([x * (i+1) for i, (x, y, z) in enumerate(past_values)]) / weighted_avg_denominator
        y_smooth = sum([y * (i+1) for i, (x, y, z) in enumerate(past_values)]) / weighted_avg_denominator
        z_smooth = sum([z * (i+1) for i, (x, y, z) in enumerate(past_values)]) / weighted_avg_denominator
        # update the position of the bird using the smoothed coordinates
        #x, y, z = x_smooth, y_smooth, z_smooth

        bird_img2 = bird_img1[0]
        if x >= 0 and x <= 1:
            x1 = (-x_smooth+1)*WIN_WIDTH
            y1 = y_smooth*WIN_HEIGHT
            if z<=0 and z>=-1:
                scaled_bird_img = pygame.transform.scale(bird_img2, (Bird_Width*(0.7-z_smooth*3), Bird_Height*(0.7-z_smooth*3)))
                bird_img[0] = scaled_bird_img
            else:
                scaled_bird_img = pygame.transform.scale(bird_img2, (Bird_Width, Bird_Height))
                bird_img[0] = scaled_bird_img
        else:
            x1 = 0.5*WIN_WIDTH
            y1 = 0.5*WIN_HEIGHT

        #x1, y1 = pyautogui.position()
        #time.sleep(1)
        print("x1", x_smooth, "y1", y_smooth, "z1", z_smooth)

        bird1 = Bird(x1, y1)
        draw_window(WIN, bird1)

"""
if __name__ == "__main__":
    main()
"""

