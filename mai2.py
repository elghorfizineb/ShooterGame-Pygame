import pygame
from game import Game
#from projectile import Projectile
pygame.init()

# #on va creer un seconde classe qui va representer le jeu
# 
# class Game :
#     
#     def __init__(self):
#         self.player = Player()
#     
# 
# 
# #on va creer une classe Joueur
# 
# class Player(pygame.sprite.Sprite):
#     
#     def __init__(self):
#         super().__init__()
#         self.health = 100
#         self.max_health = 100
#         self.attack = 10
#         self.velocity =  5
#         self.image =  pygame.image.load("assets/player.png")
#         self.rect = self.image.get_rect()
#         self.rect.x= 400
#         self.rect.y=500
#          


#generer ma fenetre


pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))

#charger le jeu qui va charger un joueur

game = Game()

#importer l'arriere plan

background = pygame.image.load("assets/bg.jpg")

running = True

#boucle tant que cette condition est vrai

while running :
    
    #premiere instructions
    #boucle qui se repete tant que le jeu est actif
    
    #appliquer l'arriere plan
    
    screen.blit(background,(0,-200))
    
    # applicquer image du joueur
    
    screen.blit(game.player.image,game.player.rect)
    
    #recuperer les projectiles du joueur
    
    for projectile in game.player.all_projectiles:
        projectile.move()
        
    #recuperer les monstres du jeu
    
    for monster in game.all_monsters:
        monster.forward()
        
    
    
    #appliquer l'ensemble des images de mon groupe de projectiles
    #fonction draw permet d'appliquer cette image sur notre ecran
    game.player.all_projectiles.draw(screen)
    
    
    #appliquer l'ensemble des images du groupe de monstre
    
    game.all_monsters.draw(screen)
    
    
    
    #verifier si un joueur veut aller a gauche ou a droite
    
    if game.pressed.get(pygame.K_RIGHT)and  game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.move_left()
        
    print(game.player.rect.x)
    
    #mettre a jour l'ecran
    
    pygame.display.flip()
    
    #si joueur ferme la fenetre
    
    for event in pygame.event.get():
        #event est fermetrure de fenetre
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            #print("femerture de jeu")
            
        #Detecter si un joueur lache une touche du clavier
            
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True
            
            #detecter si la touche espace est enclenché pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
           
                
         
        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False
#             
                 
            #quel touche a ete utilise
            
#             if event.key == pygame.K_RIGHT :
#                 game.player.move_right()
#                 
#                 #print("Deplacement vers la droite")
#                 
#             elif event.key == pygame.K_LEFT :
#                 game.player.move_left()
#                 #print("Deplacement vers la gauche")
#                 
#                 
        
        
    
    
    




