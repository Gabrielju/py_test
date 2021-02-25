import pygame

#class projectil
class Projectile(pygame.sprite.Sprite):

    #constructeur de class
    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        #redimansion du projectil
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        #position projectil
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        #présèrve l'image de base pour le tournie
        self.origin_image = self.image
        self.angle = 0

    # tourinie du projo
    def rotate(self):
        #rotation image projo
        self.angle += 3
        self .image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        #réassigne le centre de l'image pour rotate
        self.rect = self.image.get_rect(center=self.rect.center)
    # retire le projectile
    def remove(self):
        self.player.all_projectiles.remove(self)

    #vitesse projectil apliquer
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #vérifier collison monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            #supression projectil
            self.remove()
            #ifliger degas
            monster.damage(self.player.attack)

        #vérifie si le projectil est présant a l'écrant
        if self.rect.x > 1080:
            # supréssion projectil hore écrant
            self.remove()
            #print("ps")