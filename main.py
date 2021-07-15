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
asteroid_count = 5

def init():
  global asteroid_count
  global asteroids
  asteroids.empty
  for i in range(asteroid_count):
    ran_x = random.randint(50, width - 50)
    ran_y = random.randint(15,60)
    ran_size = random.randint(30, 60)
    asteroids.add(Asteroid((ran_x, ran_y), ran_size))

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
    was_hit = pygame.sprite.spritecollide(player, asteroids, True)
    if was_hit:
      player.health -= 20
      print('ship was hit. health is', player.health)
      if player.health == 0:
        print('game over')
    asteroids.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.update()

if __name__ == '__main__':
  main()