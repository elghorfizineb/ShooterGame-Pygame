import pygame

#On a gerer la notions de monstre : momie
class Monster(pygame.sprite.Sprite):
    #on definit le constructeur 
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health=100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 2
        
    def forward(self):
        #le deplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        