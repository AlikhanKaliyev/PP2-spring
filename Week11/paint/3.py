import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
lol=RED
greg=RED

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None
screen.fill(WHITE)
pygame.draw.rect(screen,BLACK,(500,0,600,100))
pygame.draw.rect(screen,WHITE,(500,100,600,200))
pygame.draw.rect(screen,BLUE,(500,200,600,300))
pygame.draw.rect(screen,GREEN,(500,300,600,400))
pygame.draw.rect(screen,RED,(500,400,600,500))
pygame.draw.line(screen,BLACK,(500,0),(500,600))
k=5
t=1
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      e= pygame.mouse.get_pos()
      if e[0]<500:
        prev = pygame.mouse.get_pos()
        
    if event.type == pygame.MOUSEMOTION:
      e= pygame.mouse.get_pos()
      if e[0]+t<499:
        cur = pygame.mouse.get_pos()
        if prev:
          pygame.draw.line(screen, lol, prev, cur, t)
          prev = cur
    if event.type == pygame.MOUSEBUTTONUP:
      a=pygame.mouse.get_pos()
      if a[0]>500 and a[1]<100:
        lol=BLACK
        greg=BLACK
      if a[0]>500 and (a[1]>100 and a[1]<200):
        lol=WHITE
        greg=WHITE
      if a[0]>500 and (a[1]>200 and a[1]<300):
        lol=BLUE
        greg=BLUE
      if a[0]>500 and (a[1]>300 and  a[1]<400):
        lol=GREEN
        greg=GREEN
      if a[0]>500 and (a[1]>400 and a[1]<500):
        lol=RED
        greg=RED
      prev = None
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        b=pygame.mouse.get_pos()
        if b[0]+k<500:
          pygame.draw.circle(screen,lol,(b[0],b[1]),k,1)
      if event.key == pygame.K_UP:
        k+=1
      if event.key == pygame.K_DOWN:
        if k>0:
          k-=1
      if event.key == pygame.K_2:
        b=pygame.mouse.get_pos()
        if b[0]+k<500:
          pygame.draw.rect(screen,lol,(b[0],b[1],k,k),1)
      if event.key == pygame.K_3:
        t=20
        lol=WHITE
      if event.key == pygame.K_4:
        t=1
        lol=greg



    

  # if prev:
  #   pygame.draw.circle(screen, RED, prev, 10)

  pygame.display.flip()

  clock.tick(30)

pygame.image.save(screen,'Untitled.png')
pygame.quit()