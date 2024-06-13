import scenes
import pygame
class Player(scenes.Movable_Game_Object):
    def __init__(self, surface, cords,screen,pygame) -> None:
        super().__init__(surface, cords)
        self.screen = screen
        self.pygame = pygame
        self.speed = 1
        self.speed_vector = [0,0]
    def update(self):#управление игроком
        super().update()
        self.move()
        #
        #
        #
        #
    def move(self):#Метод отвечает за движение по кнопкам.
        keys = self.pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_vector[0] = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.speed_vector[0] = self.speed
        elif keys[pygame.K_DOWN]:
            self.speed_vector[1] = self.speed
        elif keys[pygame.K_UP]:
            self.speed_vector[1] =- self.speed
        else:
            self.speed_vector = [0,0]
        
