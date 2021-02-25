import pygame
import math
from game import Game
pygame.init()


#generer la fenètre de jeux
pygame.display.set_caption("game title")
screen = pygame.display.set_mode((1080, 720))

#importation ressour asset arrière plan
background =pygame.image.load('assets/bg.jpg')

#charger bannier
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#charger le bouton de lancement

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y =math.ceil(screen.get_height() / 2)

#charger le jeux
game = Game()

running = True

#boucle pour executer tant que True
while running:

    #applique la boucle background
    screen.blit(background, (0, -200))

    #vérifi si le jeux commance
    if game.is_playing:
        # déclancher instruction partie
        game.update(screen)
    #vérifier si na pas commancer
    else:
        #ajout écrant de départ
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #print(game.player.rect.x)

    #mise a jour écrant
    pygame.display.flip()

    #si le joueur fèrme la fenètre
    for event in pygame.event.get():
        #vérification event est fermetur fenètre
        if event.type == pygame.QUIT:
            runnig = False
            pygame.quit()
            print("fermetur du jeux")
        #détection touche clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détection touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # savoir si la souri clic sur le boutton
            if play_button_rect.collidepoint(event.pos):
                #mètre le jeux en mod lancé
                game.start()




