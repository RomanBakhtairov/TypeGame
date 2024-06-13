import scenes
import pygame
import player
import numpy
import enemy
import test_scene
class GameScene(scenes.Scene):
    def find_fact_cords(self,screencords):# cords по факту координаты для отрисовки объектов, это не фактические координаты, поэтому преобразуем с помощь якоря
        return (numpy.array(screencords) - numpy.array(self.anchor.cords))


    def update(self):
        self.screen.fill((100,100,100))
        self.my_Text_Table.update_drower(self.objects,self.events)
        dx,dy = self.player_obj.speed_vector
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
        anchor =  pygame_module.Surface((1,1))
        icon = pygame.image.load(scenes.Scene.IM_path + 'icon.png').convert_alpha()
        enem =  pygame_module.Surface((50,50))
        enem.fill('Red')
        #
        #
        #Создаём объекты
        self.my_Text_Table = test_scene.Text_Table(self.screen_size, [800,40], 20, self.font)
        self.player_obj = player.Player(self.player, [self.screen_size[0]//2, self.screen_size[1]//2], screen, pygame_module)
        self.enemy = enemy.Enemy(enem, [self.screen_size[0]//2+ 600, self.screen_size[1]//2], self.player_obj)
        self.icontest = scenes.Movable_Game_Object(icon, [100,110])
        self.anchor =  scenes.Movable_Game_Object(anchor, [0,0])
        self.my_Text_Table = test_scene.Text_Table(self.screen_size, [800,40], 20, self.font)

        

        #
        #
        #Добавляем новоиспечённые объекты в переменную для отрисовки
       
        self.objects.append(self.enemy)
        self.objects.append(self.icontest)
        self.objects.append(self.player_obj)
        self.objects.append(self.anchor)
        self.my_Text_Table.add_to_drower(self.objects)






