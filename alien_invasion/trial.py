import pygame
from pygame import font
pygame.init()
pygame.font.init()
background_colour = (255,255,255)
(width, height) = (1200, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))
screen.blit(textsurface,(0,0))