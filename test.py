import pygame
#init elle pemet d'initialiser la bibliotheque Pygame
from gametest import Game
pygame.init()

#generer notre fenetre

#Donner un titre
pygame.display.set_caption("Shooter game")


#Donner des dimensions : largeur, longeur
screen = pygame.display.set_mode((1080,720))

#Creation d'une instance de jeu
game = Game()

#importer/charger l'arriere plan

background = pygame.image.load("assets/bg.jpg")





#controleur

running = True #booleene : true ou false

while running :
    
    #premiere instructions
    #boucle qui se repete tant que le jeu est actif
    
    #blit 
    screen.blit(background,(0,-200))
    
    #screen.blit(game.player.image,game.player.rect)
    
    
    #mettre a jour l'ecran
    pygame.display.flip()
    
    #Boucle d'evenement 
    for event in pygame.event.get():
        
        #Si tu quittes la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("On quitte le jeu")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



