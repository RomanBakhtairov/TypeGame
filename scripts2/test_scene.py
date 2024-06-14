import scenes
import pygame
import numpy
class TestScene(scenes.Scene):
    def start(self, screen, pygame_module):# просто выгружаем очень все файлы и добавляем их в objects, что отрисовывать их
        super().start(screen, pygame_module)
        screen.fill('Black')
        #
        #
        self.my_Text_Table = Text_Table(self.screen_size, [800,40], 20, self.font)
        #
        #
 #       self.my_Text_Table.add_to_drower(self.objects)

    def update(self):# здесь происходит отслеживание нажатия на кнопку
        super().update()
      #  print(len(self.objects))
        self.my_Text_Table.update_drower(self.objects,self.events)


class Text_Table:
    def deleteObjects(self):
        for i in self.myTableObjects:
            i.surface = pygame.Surface((0,0))
        for i in self.myTextObjects:
            i.surface = pygame.Surface((0,0))
        self.inWork = False
    def __init__(self,screen_size, width_and_hight,  y_cord,font) -> None:
        self.currentcords = [screen_size[0]//2 - width_and_hight[0]//2 , y_cord]
        self.width_and_hight = width_and_hight
        self.font = font
        self.texts = []
        self.texts.append('Заходит, значит, Штирлиц в бар...')
        self.myTableObjects = []
        self.myTextObjects = []
        self.myTableSurf =  pygame.Surface((width_and_hight[0],width_and_hight[1]))
        self.myTableSurf.fill("White")
        self.inWork = True
        #
        #
        #
        self.myTableObjects.append(scenes.GameObject(self.myTableSurf, [i for i in self.currentcords]))
        self.myTextObjects.append(scenes.GameObject(self.font.render(self.texts[-1], True, 'Black'), [i for i in self.currentcords]))
        #
        #
        #
    def key_event_handler(self, event):
        if self.inWork:
            if pygame.K_BACKSPACE == event.key:
                if (self.texts[-1] != ''):
                    d = self.texts[-1] 
                    self.texts[-1] = d[:-1]
                elif len(self.myTableObjects)> 1:
                    self.currentcords[1] -= self.width_and_hight[1]
                    self.texts = self.texts[:-1]
                    self.myTableObjects = self.myTableObjects[:-1]
                    self.myTextObjects = self.myTextObjects[:-1]

            else:   
                if self.font.size(self.texts[-1]+event.unicode)[0] >= self.width_and_hight[0]:
                    self.currentcords[1] += self.width_and_hight[1]
                    self.texts.append(event.unicode)
                    self.myTableObjects.append(scenes.GameObject(self.myTableSurf,[i for i in self.currentcords]))
                    self.myTextObjects.append(scenes.GameObject(self.font.render(self.texts[-1], True, 'Black'), [i for i in self.currentcords]))
                else:
                    self.texts[-1] += event.unicode
            self.myTextObjects[-1].surface = self.font.render(self.texts[-1], True, 'Black')

    def return_objects_for_draw(self):

        a =self.myTableObjects
        b =  self.myTextObjects 
        return  a+b
    def add_to_drower(self,objects):
        for i in self.return_objects_for_draw():
            objects.append(i)

    def update_drower(self, objects,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.key_event_handler(event)
        Table_objects_for_add  = []
        Text_objects_for_add= []
       
 #       print(str(len(self.myTableObjects)), ' ', str(len(objects)))
        for i in self.myTableObjects:
            flag = True
            for c in objects:
          #      print(str(i.id),' ', str(c.id))
                if c.id == i.id:
                    flag = False      
            if flag:
          #      print('there is')
                Table_objects_for_add.append(i)
             
                
       
        for i in self.myTextObjects:
            flag = True 
            for c in objects:
                if c == i:
                    flag = False
            if flag:
                Text_objects_for_add.append(i)
        #
        #
        #
        for i in Table_objects_for_add+Text_objects_for_add:
            objects.append(i)
    def return_my_text(self):
        c = ''
        for i in self.texts:
            c+= i 
        return c

    def write_text(self,string):
            self.inWork = False
            flag = True
            while flag:
                if (self.texts[-1] != ''):
                    d = self.texts[-1] 
                    self.texts[-1] = d[:-1]
                elif len(self.myTableObjects)> 1:
                    self.currentcords[1] -= self.width_and_hight[1]
                    self.texts = self.texts[:-1]
                    self.myTableObjects = self.myTableObjects[:-1]
                    self.myTextObjects = self.myTextObjects[:-1]
                else:
                    flag = False
                self.myTextObjects[-1].surface = self.font.render(self.texts[-1], True, 'Black')    
            for i in string:

                if self.font.size(self.texts[-1]+i)[0] >= self.width_and_hight[0]:
                    self.currentcords[1] += self.width_and_hight[1]
                    self.texts.append(i)
                    self.myTableObjects.append(scenes.GameObject(self.myTableSurf,[i for i in self.currentcords]))
                    self.myTextObjects.append(scenes.GameObject(self.font.render(self.texts[-1], True, 'Black'), [i for i in self.currentcords]))
                else:
                    self.texts[-1] += i
                self.myTextObjects[-1].surface = self.font.render(self.texts[-1], True, 'Black')        


                

