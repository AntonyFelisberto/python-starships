import pygame
from inimigo import Inimigo
from fire import Fire

ANCORA = 800
ALTURA = 600
FPS = 60

consolas = pygame.font.match_font("consolas")
times = pygame.font.match_font("times")
arial = pygame.font.match_font("arial")
courier = pygame.font.match_font("courier")

BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (255,0,0)
H_FA2F2F = (250,47,47)
GREEN= (0,255,0)
BLUE = (0,0,255)

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
        self.cadencia = 300
        self.ultimate = pygame.time.get_ticks()
    
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
        if teclas[pygame.K_SPACE]:
            tempo = pygame.time.get_ticks()
            if tempo - self.ultimate > self.cadencia:
                laser.set_volume(0.2)
                laser.play()
                self.disparos_um()
                self.disparos_dois()
                self.ultimate = tempo

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
    
    def disparos_um(self):
        bala =  Fire(self.rect.centerx - 30,self.rect.centery + 20)
        balas.add(bala)

    def disparos_dois(self):
        bala =  Fire(self.rect.centerx + 30,self.rect.centery + 20)
        balas.add(bala)

def texto(tela,fonte,texto,cor,dimensoes,x,y):
    tipo_letra = pygame.font.Font(fonte,dimensoes)
    superficie = tipo_letra.render(texto,True,cor)
    retangulo = superficie.get_rect()
    retangulo.center = (x,y)
    tela.blit(superficie,retangulo)

laser = pygame.mixer.Sound("arquivos\\sounds\\disparo.wav")
pontos = pygame.mixer.Sound("arquivos\\sounds\\point.wav")
ambiente = pygame.mixer.Sound("arquivos\\sounds\\sonido_fondo.mp3")

ambiente.set_volume(0.5)
ambiente.play()

tela = pygame.display.set_mode((ANCORA,ALTURA))

fundo = pygame.transform.scale(pygame.image.load("arquivos\\images\\OIP.jpg").convert(),(1000,600))

clock = pygame.time.Clock()

jogador = pygame.sprite.Group()
jogadores = Player()
jogador.add(jogadores)

inimigo = pygame.sprite.Group()
balas = pygame.sprite.Group()

executando = True
pontuacao = 0
while executando:
    clock.tick(FPS)
    tela.blit(fundo,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    texto(tela,times,str(pontuacao).zfill(3),WHITE,50,700,50)

    jogador.update()
    inimigo.update()
    balas.update()
    colisao_nave = pygame.sprite.groupcollide(inimigo,jogador,False,False)
    colisao_bala = pygame.sprite.groupcollide(inimigo,balas,True,True)

    if colisao_nave:
        pontuacao -= 10

    if pontuacao < 0:
        pontuacao = 0
        jogadores.kill()
        inimigos.kill()
        break

    if colisao_bala:
        pontos.set_volume(0.1)
        pontos.play()
        pontuacao += 30

    if pontuacao > 1000:
        jogadores.cadencia + 100

    if not inimigo:
      for x in range(5):
        inimigos = Inimigo()
        inimigo.add(inimigos)  
    
    jogador.draw(tela)
    inimigo.draw(tela)
    balas.draw(tela)
    pygame.display.flip()
