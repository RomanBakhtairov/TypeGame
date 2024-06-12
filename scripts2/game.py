import pygame 
import scenes as sc
import open_scene as op
import game_scene as gm
class Game:
    IMAGE_PATH = '../python game/images/'
    #
    def __init__(self,start_scene: sc.Scene) -> None:
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
            self.current_scene.update()
            #
            #
            #
            pygame.display.update()
            #
            #
            #
            if self.current_scene.TriggerFlag:
                self.current_scene =self.current_scene.to_next_scene()
                self.current_scene.start(self.screen, pygame)
            #
            #
            #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_in_run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.screen = pygame.display.set_mode((600, 400))
                        
    #



if __name__ == '__main__':
    pygame.init()
    newscene = op.StartScene()
    game_scene = gm.GameScene()
    my_game = Game(newscene)