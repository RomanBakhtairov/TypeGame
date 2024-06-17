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
        enem =  pygame.transform.scale(enem, (150,150))
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

        self.enemy_list =[]
        def create_enemy(cords):
             my_enemy = enemy.Enemy(enem, [self.screen_size[0]//2+ cords[0], self.screen_size[1]//2+ cords[1]], self.player_obj)
             my_enemy.set_texters(self.interactive_text, self.my_Text_Table)
             my_enemy.add_animation_keys(6,  scenes.Scene.IM_path + 'проект питон/enemy_3/enemy_3_right_e/','right', 150)
             my_enemy.add_animation_keys(6,  scenes.Scene.IM_path + 'проект питон/enemy_3/enemy_3_left_e/','left', 150)
             self.enemy_list.append(my_enemy)
        #
        #
        create_enemy([0,700])
        create_enemy([1400,0])
        create_enemy([-1400,0])
        #
        #
        #Добавляем новоиспечённые объекты в переменную для отрисовки
        self.objects.append(self.map)
        for i in self.enemy_list:
            self.objects.append(i)
        self.objects.append(self.player_obj)
        self.objects.append(self.anchor)
        self.my_Text_Table.add_to_drower(self.objects)
        self.objects.append(self.health_bar)






