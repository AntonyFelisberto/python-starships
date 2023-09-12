import pygame
from inimigo import Inimigo

ANCORA = 800
ALTURA = 600
FPS = 60

class Inicio():
    pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load("arquivos\\images\\nave-espacial.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400,550)
        self.velocidade_x = 0
        self.velocidade_y = 0
    
    def update(self):
        self.velocidade_x = 0
        self.velocidade_y = 0
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]:
            self.velocidade_x = -10
        if teclas[pygame.K_d]:
            self.velocidade_x = 10
        if teclas[pygame.K_w]:
            self.velocidade_y = -10
        if teclas[pygame.K_s]:
            self.velocidade_y = 10

        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.right > ANCORA:
            self.rect.right = ANCORA

        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
            
        if self.rect.top < 0:
            self.rect.top = 0      

tela = pygame.display.set_mode((ANCORA,ALTURA))

fundo = pygame.transform.scale(pygame.image.load("arquivos\\images\\OIP.jpg").convert(),(1000,600))

clock = pygame.time.Clock()

jogador = pygame.sprite.Group()
jogadores = Player()
jogador.add(jogadores)

inimigo = pygame.sprite.Group()
inimigos = Inimigo()
inimigo.add(inimigos)

executando = True

while executando:
    clock.tick(FPS)
    tela.blit(fundo,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    jogador.update()
    inimigo.update()
    jogador.draw(tela)
    inimigo.draw(tela)
    pygame.display.flip()
