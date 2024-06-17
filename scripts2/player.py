import scenes
import pygame
class Player(scenes.Movable_Game_Object):
    def __init__(self, surface, cords,screen,pygame) -> None:
        super().__init__(surface, cords)
        self.killed_enemy_counter = 0
        self.health = 100
        self.screen = screen
        self.pygame = pygame
        self.speed = 1
        self.speed_vector = [0,0]
        self.inbattle = False
    def update(self):#управление игроком
        super().update()
        if not(self.inbattle) and self.health > 0:
            self.move()
        else:
            self.speed_vector = [0,0]

        if self.health <=0:
            self.die()
        #
        #
        #
        #
    def move(self):#Метод отвечает за движение по кнопкам.
        self.keys = self.pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:
            self.speed_vector[0] = -self.speed
        elif self.keys[pygame.K_RIGHT]:
            self.speed_vector[0] = self.speed
        elif self.keys[pygame.K_DOWN]:
            self.speed_vector[1] = self.speed
        elif self.keys[pygame.K_UP]:
            self.speed_vector[1] =- self.speed
        else:
            self.speed_vector = [0,0]
    def we_kill_enemy(self):
        self.killed_enemy_counter +=1
        if self.killed_enemy_counter ==3:
            c = pygame.font.Font('../python game/font/Roboto-Black.ttf',45)
            for i in range(len(self.animation_left)):
                a =  c.render('Вы выиграли!',True,'Black', 'White')
                self.animation_left[i] = a
                self.animation_right[i] =a

    def die(self):
        super().die()
        self.animation_left[0] = Player.die_image
        self.animation_right[0] =Player.die_image

class Heelth_bar(scenes.GameObject):
    def __init__(self,player, surface = pygame.Surface((200, 20)), cords = [10, 40]) -> None:
        super().__init__(surface, cords)
        self.player = player
    def update(self):
        super().update()
        self.surface = pygame.Surface((self.player.health*2, 20))
        self.surface.fill("Red")
        self.cords = [10, 40]
    

        
