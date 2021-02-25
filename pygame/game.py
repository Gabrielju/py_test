from player import Player
from monster import Monster
import pygame


#créer seconde calss game
class Game:

    def __init__(self):
        #défini si le jeux commance ou non
        self.is_playing = False
        # génération du joueur
        self.all_player = pygame.sprite.Group()
        #group sprite joueur et collision
        self.player = Player(self)
        self.all_player.add(self.player)
        #group monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remètre le jeux a nef retitrer monstre recharger pv
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'imge du player
        screen.blit(self.player.image, self.player.rect)

        # actualiser la bar de vi player
        self.player.update_health_bar(screen)

        # application img projectile
        self.player.all_projectiles.draw(screen)

        # appliquer les monstre
        self.all_monster.draw(screen)

        # réqupérer les projectil du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # réqupérer les monstre
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        # détection des touche de déplacement
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    #closision monstre/ entiter False pour ne pas mourir en collision collide_mask = itbox
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)