import scenes
import pygame
class StartScene(scenes.Scene):
    def start(self, screen, pygame_module):
        super().start(screen, pygame_module)
        self.flag = True
        self.texter = self.font.render('Начать игру', False, 'White')
        self.button_im = pygame_module.image.load(scenes.Scene.IM_path + 'button2.png')
        self.button = Button(self.texter, self.button_im,[450,300])
        self.objects.append( self.button.frame)
        self.objects.append( self.button.text)
    def update(self):
        super().update()
        mouse = self.pygame_module.mouse.get_pos()
        if self.button.rect.collidepoint(mouse) and self.pygame_module.mouse.get_pressed()[0] and self.flag:
            self.flag = False
            self.TriggerFlag = True
    
        






class Button:
    def __init__(self,text_surface,frame_surface, cords) -> None:
        self.text = scenes.GameObject(text_surface, [cords[0]+ 145 , cords[1] + 30])
        self.frame = scenes.GameObject(frame_surface, cords)
        self.rect = frame_surface.get_rect(topleft = cords)
        self.frame.cords = self.rect
        self.module  = pygame

          