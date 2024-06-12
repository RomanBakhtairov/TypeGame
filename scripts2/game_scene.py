import scenes
import pygame
class GameScene(scenes.Scene):
    def update(self):
        self.screen.fill((100,100,100))
        dx,dy = self.player_obj.player_speed_vector
        super().update(relativespeed=[-dx, -dy])
        
        '''Важное примечание. Тут фигурирует идея относительной и абсолютной скорости. Относительная будет работать на все объект
        на сцене, которые можно двигать(Movable_Game_Object). Она зависит от скорости игрока. Вообще я сделал в тупую
        - если player движется, то всё окружающее пространство будет двигаться напротив(создавая иллюзию
        передвижения), а у самого игрока абсолютная и относительная 
        скорость компенсируется в ноль'''
    

    def start(self, screen, pygame_module):

        super().start(screen, pygame_module)
        self.screen.fill((100,100,100))
        self.background = pygame_module.image.load(scenes.Scene.IM_path + 'map.jpg')
        #
        self.player = pygame_module.Surface((50,50))#Пространство, чтобы поменять код
        self.player.fill("Blue")
        #
        icon = pygame.image.load(scenes.Scene.IM_path + 'icon.png').convert_alpha()
        self.player_obj = player(self.player, [self.screen_size[0]//2, self.screen_size[1]//2], screen, pygame_module)
        self.icontest = scenes.Movable_Game_Object(icon, [100,110])
        self.objects.append(self.icontest)
        self.objects.append(self.player_obj)






class player(scenes.Movable_Game_Object):
    def __init__(self, surface, cords,screen,pygame) -> None:
        super().__init__(surface, cords)
        self.screen = screen
        self.pygame = pygame
        self.speed = 1
        self.player_speed_vector = [0,0]
    def update(self):#управление игроком
        super().update()
        keys = self.pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_speed_vector[0] = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.player_speed_vector[0] = self.speed
        elif keys[pygame.K_DOWN]:
            self.player_speed_vector[1] = self.speed
        elif keys[pygame.K_UP]:
            self.player_speed_vector[1] =- self.speed
        else:
            self.player_speed_vector = [0,0]
        
        x,y = self.cords
        xs,ys = self.player_speed_vector
        self.cords = [x+xs, y+ys]
