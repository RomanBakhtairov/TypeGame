import pygame 
import scenes as sc
import open_scene as op
import game_scene as gm
import test_scene as ts
class Game: #Главный игровой класс, для его создания нужна самая первая сцена. В самом низу создаем экзмпляр класса
    IMAGE_PATH = '../python game/images/'
    #
    def __init__(self,start_scene: sc.Scene) -> None: #Содержание можно не трогать
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("THE GREAT GAME")
        icon = pygame.image.load(Game.IMAGE_PATH + 'icon.png').convert_alpha()
        pygame.display.set_icon(icon)
        self.game_in_run = True
        self.current_scene = start_scene
        start_scene.start(self.screen, pygame)

        while self.game_in_run:
            #
            #
            #
            self.current_scene.update() #update по содержанию сцены
            #
            #
            #
            pygame.display.update() #Отрисовка
            #
            #
            #
            self.current_scene.events = pygame.event.get()
            #
            #
            #
            if self.current_scene.TriggerFlag: #Проверяет, нужно ли скакнуть на следущую сцену
                self.current_scene = self.current_scene.to_next_scene() #Он помнит все созданные сцены и просто перейдёт к сцене, созданной после этой
                self.current_scene.start(self.screen, pygame)
            #
            #
            #
            for event in self.current_scene.events: #Отвечает за нажатие esc
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_in_run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.screen = pygame.display.set_mode((1200, 600))
                        
    #



if __name__ == '__main__':
    pygame.init() #Это для pygame 
    newscene = op.StartScene() #Создаем сцены в порядке следования
    game_scene = gm.GameScene()
    my_game = Game(newscene)
    
