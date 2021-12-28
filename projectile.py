import pygame
#from player import Player

#On va ajouter un heritage pour definir un sprite
class Projectile(pygame.sprite.Sprite):
    #definir le constructeur de cette classe
    
    #on va ajouter un object player dans le constructeur pour lui associer un projectile
    def __init__(self,player):
        #super constructeur
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        #elle permet de redimensionner l'image en donnant l'image et sa taille avec largeuur et hauter
        self.image = pygame.transform.scale(self.image,(50,50))
        #placer et deplacer l'image
        self.rect = self.image.get_rect()
        #On recupere les coordonnées afin de pouvoir le placer a coté du joueur
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        #2 nouveau attributs
        #On dit qu'on doit garder l'image d'origine
    
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        #tourner le projectiles
        self.angle += 30
        #On va transformer l'image avec rotozoom qui prend 3 attributs
        #l'image originel
        #l'angle de rotaton
        #scale = 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def remove(self) :
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        # Si le projectile entre en collision avec un monstre
        if self.player.game.check_collision(self,self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()

    
        
        #On va verifier si notre projectiles n'est plus dans l'ecran
        
        if self.rect.x > 1080:
            #supprimer le projectile (en dehors de l'ecren)
            #on va recuperer le sprite et supprimer l'object courant
            self.remove()
            
            
            
            
            