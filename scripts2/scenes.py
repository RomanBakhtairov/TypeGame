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
    def __init__(self, surface, cords) -> None:
        super().__init__(surface, cords)
        self.type_in_str = 'Movable_Game_Object'
        self.speed = 0
        self.speed_vector = [0,0]
    def update(self):
        super().update()
        x,y = self.cords
        xs,ys = self.speed_vector
        self.cords = [x+xs, y+ys]
        

if __name__ == "__main__":
    gost = pygame.image.load('../python game/images/gost.png')

if __name__ == "__main__":
    gost = pygame.image.load('../python game/images/gost.png')