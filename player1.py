import pygame

class Player(pygame.sprite.Sprite):
    def __init__():
        #Super - constructeur 
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 15
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x= 400
        self.rect.y=500
    
    #2 methodes : fonctions du joueur
    def move_right():
        self.rect.x = self.rect.x + self.velocity

        
    def move_left():
        self.rect.x = self.rect.x - self.velocity