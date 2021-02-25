import pygame
import random


#créer une première class pour les monstres
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        #stat
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 2)
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 980 + random.randint(0, 300)
        self.rect.y = 550

    def damage(self, amount):
        #infliger degas
        self.health -= amount

        #vérifier les pv nombre
        if self.health <= 0:
            #recharge entitée
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

    def update_health_bar(self, surface):

        #dessin bar pv
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 12, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 12, self.rect.y - 20, self.health, 5])

    def forward(self):
        #déplacement si pas de collision avec player
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        #si le monstre rentre dans le player
        else:
            #infliger des degas
            self.game.player.dammage(self.attack)