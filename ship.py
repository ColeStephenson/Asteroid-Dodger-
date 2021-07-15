import pygame
import json

class Ship(pygame.sprite.Sprite):

  def __init__(self, pos):
    super().__init__()
    self.player_data = json.load(open('game.json', 'rb'))['player']
    self.image = pygame.image.load('ship.png')
    self.image = pygame.transform.smoothscale(self.image, (30, 60))
    self.image = pygame.transform.rotate(self.image, -90)
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.health = self.player_data['health']
    self.speed = pygame.math.Vector2(0, 0)
  
  def update(self):
    self.rect.move_ip(self.speed)

