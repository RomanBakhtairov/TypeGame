import pygame

class Scene:
    my_scenes = []
    IM_path = '../python game/images/'
    def __init__(self):
        self.objects = []
        Scene.my_scenes.append(self)
        self.events = []
        
    def update(self,  relativespeed = [0,0]):
        screen = self.screen
        pygame_module = self.pygame_module
        self.screen_size = screen.get_size()
        for i in self.objects:
            i.update()
            self.screen.blit(i.surface, i.cords)
            if i.type_in_str == 'Movable_Game_Object':
                x,y = i.cords[:2]
                xs, ys = relativespeed[:2]
                i.cords = [x + xs, y + ys]
    def start(self, screen, pygame_module):
        self.screen_size = screen.get_size()
        self.TriggerFlag = False
        self.font = pygame.font.Font('../python game/font/Roboto-Black.ttf',25)
        self.pygame_module = pygame_module
        self.screen = screen
    def to_next_scene(self):# Найдет нашу сцены среди сохранённых и передаст следующую созданную
        index = 0
        for i in range(len(Scene.my_scenes)):
            if Scene.my_scenes[i] == self:
                index = i
                break
        return Scene.my_scenes[index+1]

class GameObject:
    
    current_id = 0
    def __init__(self,surface, cords) -> None: # где cords кортеж
        self.type_in_str = 'GameObject'
        self.surface = surface
        self.cords = cords 
        self.id = GameObject.current_id
        GameObject.current_id += 1

    def update(self):
        pass

class Movable_Game_Object(GameObject):
    die_image = pygame.Surface((50,50))
    def __init__(self, surface, cords) -> None:
        super().__init__(surface, cords)
        self.base_surf = surface
        self.animation_updater = 50
        self.animation_update_check = 0
        self.animation_right = []
        self.animation_left = []
        self.rigth_count = 0
        self.left_count = 0
        #
        #
        #
        self.type_in_str = 'Movable_Game_Object'
        self.speed = 0
        self.speed_vector = [0,0]
        self.previous_speed_vector = self.speed_vector
    def update(self):
        super().update()
        x,y = self.cords
        xs,ys = self.speed_vector
        self.cords = [x+xs, y+ys]
        #
        #
        #
        if self.animation_update_check > self.animation_updater:
            if self.speed_vector[0] > 0:
                if len( self.animation_right) > 0:
                    if self.rigth_count+1 >= len(self.animation_right):
                        self.rigth_count = 0
                    else:
                        self.rigth_count +=1
                    self.surface = self.animation_right[self.rigth_count]
            elif self.speed_vector[0] < 0:
                if len( self.animation_left) > 0:
                    if self.left_count+1 >= len(self.animation_left):
                        self.left_count = 0
                    else:
                        self.left_count +=1
                    self.surface = self.animation_left[self.left_count]
            else:
                if len(self.animation_right )> 0 and len(self.animation_left )> 0:
                    if self.previous_speed_vector[0] >0 and self.speed_vector[0] == 0:
                        self.surface = self.animation_right[0]
                    elif self.previous_speed_vector[0] <0 and self.speed_vector[0] == 0:
                       
                        self.surface = self.animation_left[0]
                else:
                    self.surface = self.base_surf
            self.previous_speed_vector = self.speed_vector
            self.animation_update_check  = 0
        else:
            self.animation_update_check +=1
      
    def add_animation_keys(self, key_number, path, anim_key):# где anim_key - код: "right" или "left"
            def return_keys(key_number, path ):
                return_massive = []
                for i in range(1, key_number):
                    c = pygame.image.load(path + str(i) + '.png').convert_alpha()
                    return_massive.append(pygame.transform.scale(c, (60,60)))
                return return_massive
            if anim_key == 'right':
                self.animation_right  = return_keys(key_number, path)
            if anim_key == 'left':
                self.animation_left  = return_keys(key_number, path)
    def die(self):
        self.surface = Movable_Game_Object.die_image
        self.animation_left[0] = Movable_Game_Object.die_image
        self.animation_right[0] =Movable_Game_Object.die_image

                
        

if __name__ == "__main__":
    gost = pygame.image.load('../python game/images/gost.png')

if __name__ == "__main__":
    gost = pygame.image.load('../python game/images/gost.png')