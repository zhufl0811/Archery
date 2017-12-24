import pygame,time
from pygame.locals import *

if __name__ == '__main__':
	screen = pygame.display.set_mode((1076,604))
	bgimg = pygame.image.load('./bg.png').convert()
	while True:
		screen.blit(bgimg,(0,0))
		pygame.display.update()
		time.sleep(0.01)
		