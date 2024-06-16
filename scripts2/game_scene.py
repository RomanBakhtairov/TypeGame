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
        self. interactive_text.update_drower(self.objects, self.events)
        dx,dy = self.player_obj.speed_vector
        super().update(relativespeed=[-dx, -dy])
        
        '''Важное примечание. Тут фигурирует идея относительной и абсолютной скорости. Относительная будет работать на все объект
        на сцене, которые можно двигать(Movable_Game_Object). Она зависит от скорости игрока. Вообще я сделал в тупую
        - если player движется, то всё окружающее пространство будет двигаться напротив(создавая иллюзию
        передвижения), а у самого игрока абсолютная и относительная 
        скорость компенсируется в ноль'''
    

    def start(self, screen, pygame_module):

        super().start(screen, pygame_module)

        #
        grave =  pygame.image.load(scenes.Scene.IM_path + 'grave.png').convert_alpha()
        scenes.Movable_Game_Object.die_image = pygame.transform.scale(grave, (60,60))
        self.player =  pygame.image.load(scenes.Scene.IM_path + '/проект питон/character/character_right/character_right_1.png').convert_alpha()
        self.player = pygame.transform.scale(self.player, (60,60))
        anchor =  pygame_module.Surface((1,1))
        map = pygame.image.load(scenes.Scene.IM_path + 'вариант1.png').convert_alpha()
        map =  pygame.transform.scale(map, (6000,4000))
        enem = pygame.image.load(  scenes.Scene.IM_path + 'проект питон/enemy_3/enemy_3_right_e/1.png').convert_alpha()
        #
        #
        #Создаём объекты
        self. interactive_text = test_scene.Text_Table(self.screen_size, [800,40], 120, self.font)
        self.my_Text_Table = test_scene.Text_Table(self.screen_size, [800,40], 20, self.font)
        self.player_obj = player.Player(self.player, [self.screen_size[0]//2, self.screen_size[1]//2], screen, pygame_module)
        self.map = scenes.Movable_Game_Object(map, [-2000,-2000])
        self.anchor =  scenes.Movable_Game_Object(anchor, [0,0])
        self.my_Text_Table = test_scene.Text_Table(self.screen_size, [800,40], 20, self.font)
        self.health_bar = player.Heelth_bar(self.player_obj )
        #Анимации
        self.player_obj.add_animation_keys(5, scenes.Scene.IM_path + '/проект питон/character/character_right/character_right_','right')
        self.player_obj.add_animation_keys(5, scenes.Scene.IM_path + '/проект питон/character/character_left/character_left_','left')



        self.enemy = enemy.Enemy(enem, [self.screen_size[0]//2+ 600, self.screen_size[1]//2], self.player_obj)
        self.enemy1 = enemy.Enemy(enem, [self.screen_size[0]//2+ 1500, self.screen_size[1]//2], self.player_obj)
        self.enemy.set_texters(self.interactive_text, self.my_Text_Table)
        self.enemy1.set_texters(self.interactive_text, self.my_Text_Table)
        #
        #Анимации противников
        self.enemy.add_animation_keys(6,  scenes.Scene.IM_path + 'проект питон/enemy_3/enemy_3_right_e/','right')
        self.enemy.add_animation_keys(6,  scenes.Scene.IM_path + 'проект питон/enemy_3/enemy_3_left_e/','left')
        self.enemy1.add_animation_keys(6,  scenes.Scene.IM_path + 'проект питон/enemy_3/enemy_3_right_e/','right')
        self.enemy1.add_animation_keys(6,  scenes.Scene.IM_path + 'проект питон/enemy_3/enemy_3_left_e/','left')


        

        #
        #
        #Добавляем новоиспечённые объекты в переменную для отрисовки
        self.objects.append(self.map)
        self.objects.append(self.enemy)
        self.objects.append(self.enemy1)
        self.objects.append(self.player_obj)
        self.objects.append(self.anchor)
        self.my_Text_Table.add_to_drower(self.objects)
        self.objects.append(self.health_bar)






