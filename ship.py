import pygame
import json

class Ship(pygame.sprite.Sprite):

  def __init__(self, pos):
    super().__init__()
    self.player_data = json.load(open('game.json', 'rb'))['player']
    self.image = pygame.image.load('ship.png')
    self.image = pygame.transform.smoothscale(self.image, (30, 60))
    self.image = pygame.transform.rotate(self.image, self.player_data['rotation'])
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.health = self.player_data['health']
    self.speed = pygame.math.Vector2(0, 0)
  
  def update(self):
    screen_info = pygame.display.Info()
    self.rect.move_ip(self.speed)
    if self.rect.left < 0 or self.rect.right >screen_info.current_w:
      self.speed [0] = 0
      self.rect.move_ip(self.speed[0], 0)
    if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
      self.speed[1] = 0
      self.rect.move_ip(0, self.speed[1])

