import pygame
import pandas
import sys
from pygame.locals import *
from ship import Ship
from asteroid import Asteroid
import random

pygame.init()
screen_info = pygame.display.Info()
width = screen_info.current_w
height = screen_info.current_h
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player = Ship((width // 2, height // 2))
asteroids = pygame.sprite.Group()
asteroid_count = 2

def init():
  global asteroid_count
  global asteroids
  asteroids.empty
  for i in range(asteroid_count):
    asteroids.add(Asteroid(
      (random.randint(50, width - 50),
      random.randint (50, height - 50)),
      random.randint(15, 60)
    ))

def main():
  init()
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit(0)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          player.speed[0] = -2
        elif event.key == pygame.K_d:
          player.speed[0] = 2
        elif event.key == pygame.K_w:
          player.speed[1] = -2
        elif event.key == pygame.K_s:
          player.speed[1] = 2
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
          player.speed[0] = 0
        elif event.key == pygame.K_d:
          player.speed[0] = 0
        elif event.key == pygame.K_w:
          player.speed[1] = 0
        elif event.key == pygame.K_s:
          player.speed[1] = 0
    screen.fill((0, 0, 0))        # comment this out for something funny ;))
    player.update()
    asteroids.update()
    asteroids.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.update()

if __name__ == '__main__':
  main()