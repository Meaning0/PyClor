#Author: StephenCurry
#Author_Email: m18824909883@163.com
#Edition: v1.0
#Last update: 2019.4.5
#import the pygame!
import pygame
# import random for random numbers!
import random
# import pygame.locals for easier access to key coordinates
from pygame.locals import *
import sys
import time
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('image/plane.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -3)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 3)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-3, 3)
