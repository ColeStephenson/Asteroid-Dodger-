import pygame
import pandas
import sys
from pygame.locals import *
from ship import Ship
from asteroid import Asteroid
import random
import json
from timer import Timer

pygame.init()
screen_info = pygame.display.Info()
width = screen_info.current_w
height = screen_info.current_h
size = (width, height)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
data = json.load(open('game.json', 'rb'))
level = 1
asteroids = None
asteroid_count = None
player = None
player_speed = None
timer = None
game_font = pygame.font.SysFont('truetype', 50)
level_image = None


def init():
  global asteroid_count
  global asteroids
  global player
  global player_speed
  global timer
  global level_image
  level_image = game_font.render(str(level), False, (255, 255, 255), (0, 0, 0))
  player_speed = level * 2
  player = Ship((width // 2, height // 2))
  asteroids = pygame.sprite.Group()
  timer = Timer(30*level)
  asteroid_count = level * 5
  asteroids.empty()
  for i in range(asteroid_count):
    ran_x = random.randint(50, width - 50)
    ran_y = random.randint(15,60)
    ran_size = random.randint(30, 60)
    asteroids.add(Asteroid((ran_x, ran_y), ran_size))

def main():
  global level
  init()
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit(0)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          player.speed[0] = -player_speed
        elif event.key == pygame.K_d:
          player.speed[0] = player_speed
        elif event.key == pygame.K_w:
          player.speed[1] = -player_speed
        elif event.key == pygame.K_s:
          player.speed[1] = player_speed
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
          player.speed[0] = 0
        elif event.key == pygame.K_d:
          player.speed[0] = 0
        elif event.key == pygame.K_w:
          player.speed[1] = 0
        elif event.key == pygame.K_s:
          player.speed[1] = 0
    screen.fill((10, 10, 10))        # comment this out for something funny ;))
    player.update()
    asteroids.update()
    if timer.is_finished():
      print('you won!')
      level = level + 1
      init()
    was_hit = pygame.sprite.spritecollide(player, asteroids, True)
    if was_hit:
      player.health -= data['asteroid']['damage']
      print('ship was hit. health is', player.health)
      if player.health == 0:
        print('game over')
        init()
    asteroids.draw(screen)
    screen.blit(player.image, player.rect)
    screen.blit(timer.get_image(game_font), (0, 0))
    pygame.display.update()

if __name__ == '__main__':
  main()