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

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("arquivos\\images\\ovni.png")
        self.rect = self.image.get_rect()
        self.rect.center = (450,500)
        self.rect.x = random.randrange(ANCORA - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)

        self.velocidade_x = random.randrange(1,10)
        self.velocidade_y = random.randrange(1,10)

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y