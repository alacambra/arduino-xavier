import sys
import pygame
pygame.init()
import PyQt4

#create the screen
window = pygame.display.set_mode((640, 480))

#draw a line - see http://www.pygame.org/docs/ref/draw.html for more
pygame.draw.line(window, (255, 255, 255), (0, 0), (30, 50))
pygame.draw.circle(window,(255, 255, 255), (50, 50), 50)
#draw it to the screen
pygame.display.flip()

#input handling (somewhat boilerplate code):
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)
      else:
          print event
