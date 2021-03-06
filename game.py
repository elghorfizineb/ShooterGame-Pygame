import pygame
from player import Player
from monster import Monster

class Game :
    
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #on va definir un groupe de monstre
        self.all_monsters= pygame.sprite.Group()
        #ici on va mettre un dictionnaire vide
        self.pressed = {}
        self.spawn_monster()
    
    def check_collision(self, sprite, group):
        #methode qui permet de comparer si un sprite entre en collision avec un groupe
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)