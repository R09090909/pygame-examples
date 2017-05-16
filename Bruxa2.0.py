#GIMP - usar p fazer fundo transparente
import pygame
import os

pygame.init()
vec = pygame.math.Vector2

largura = 800
altura = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((956, 560))

pygame.display.set_caption('Jogo da Bruxa')
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
	def __init__ (self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join("pulando.png")).convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.center = (largura/2, altura/2)
		self.y_speed = 5

	def update(self):
		self.rect.y += self.y_speed
		if self.rect.bottom > altura - 40:
			self.y_speed = 0
		if self.rect.top < 50:
			self.y_speed = 5
		#vec = pygame.math.Vector2
		#self.pos = vec(largura/2, altura/2)
		#self.rect.midbottom = self.pos

class Platform(pygame.sprite.Sprite):
	def __init__ (self, x, y, widht, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join("imagem.png")).convert()
		self.image.set_colorkey(white)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y 

class Fundo():
	def __init__(self):
		self.pos = vec(largura/2, altura/2)
		sel.vel = vec(0,0)
		self.acc = vec(0,0)

def background(x,y):
	screen.blit(backgroundload,(x,y))
def tijolo(xplat,yplat):
	screen.blit(tijoloload,(xplat,yplat))

backgroundload = pygame.image.load('big.jpg')
tijoloload = pygame.image.load('imagem.png')

## armazena todos os retangulos

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

## armazena todas as plataformas

def game_loop():
	x = (largura * 0.005)
	y = (altura * 0.0025)
	xplat = 250
	yplat = altura - 90
	x_change = 0
	y_change = 0

	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = 5
					#o boneco vai p esquerda
					#tudo tem que ir junto (os retangulos, os bonecos etc)
					
				if event.key == pygame.K_RIGHT:
					x_change = -5
					#o boneco vai p direita
					#tudo tem que ir junto (os retangulos, os bonecos etc)
				if event.key == pygame.K_UP:
					y_change = 5
					#o boneco "vai p cima
					#tudo tem que ir junto (os retangulos, os bonecos etc)
				if event.key == pygame.K_DOWN:
					y_change = -5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0

		x += x_change
		y += y_change

		#all_sprites.replace(plat)
		#platforms.add(plat)

		xplat+=x_change
		p1 = Platform(xplat,altura-90,300, 30)
		#all_sprites.blit(p1)
		#platforms.add(p1)
		#screen.blit(p1,pygame.Surface())




		pygame.display.update()
		all_sprites.update()

		hits = pygame.sprite.spritecollide(player,platforms,False)
		if hits:
			#player.pos.y = hits[0].rect.top
			player.y_speed = 0

		background(x,y)
		all_sprites.draw(screen)
		clock.tick(60)
		tijolo(xplat,yplat)
		all_sprites.draw(screen)
		clock.tick(60)

game_loop()
pygame.quit()
quit()



'''
Para mexer o oponente:
	self.rect.x += self.x_speed
		if self.rect.right > largura - 100:
			self.x_speed = -5
		if self.rect.left < 100:
			self.x_speed = 5
'''
