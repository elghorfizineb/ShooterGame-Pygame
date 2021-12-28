import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        #self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity =  5
        #on va ajouter un groupe de projectile
        self.all_projectiles = pygame.sprite.Group()
        self.image =  pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x= 400
        self.rect.y= 500
    
    def launch_projectile(self):
        #on va creer une groupe/ un objet de la classe Projectile / ensuite on lui passera l'object du joueur
        self.all_projectiles.add(Projectile(self))
   
    
    def move_right(self):
        #Si le joueur n'est pas en collision avec un entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
        
    def move_left(self):
        self.rect.x -= self.velocity