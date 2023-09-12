from typing import Any
import pygame
import random

ANCORA = 600
ALTURA = 600


BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (255,0,0)
H_FA2F2F = (250,47,47)
GREEN= (0,255,0)
BLUE = (0,0,255)

class Fire(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("arquivos\\images\\disparo.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 10

        if self.rect.bottom < 0:
            self.kill()