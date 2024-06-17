import scenes, pygame, math,random
class Enemy(scenes.Movable_Game_Object):
    CONDISIONS = ('stay','attack','chase','die', 'battle')#У противника есть разные состояния, но текущим может быть только одно
    def __init__(self, surface, cords, player_Obj) -> None:
        super().__init__(surface, cords)
        self.health = 100
        self.damage = 5
        self.ticker = 0
        self.str_text_for_question = random.choice(["Огнем и мечом",
                                      "Безупречный иней",
                                      "Из солнца и крови",
                                      "Отчуждение покровов",
                                      "Стрекотание в душе",
                                      "Вой в сердце",
                                      "Ускользающая смерть",
                                      "Неотвратимость голода",
                                      "Lorem ipsum"])
        self.player = player_Obj
        self.battle_distance = 150
        self.launch_distance = 700 #дистанция, с которой противник начинает преследовать игрока(условно - это половина ребра квадрата)
        self.attack_distance = 50 #дистанция, с которой начинается бой с противником
        self.previous_condition = self.current_condition = Enemy.CONDISIONS[0]
        self.speed = 0.9
    def find_actual_dist(self):
        self.xdist = self.player.cords[0] - self.cords[0]
        self.ydist = self.player.cords[1] - self.cords[1]
        actual_distance = (self.xdist**2 + self.ydist**2)**(1/2)
        return actual_distance
    def update(self):
        super().update()
        self.define_current_condition()
        if self.current_condition == Enemy.CONDISIONS[2] or self.current_condition == Enemy.CONDISIONS[4]:
            actual_distance = self.find_actual_dist()
            self.speed_vector = [self.xdist/actual_distance* self.speed, self.ydist/actual_distance*self.speed ]
        else:
            self.speed_vector = [0,0]
        if self.current_condition == Enemy.CONDISIONS[1]:
            self.attack(self.player)
        if self.current_condition == Enemy.CONDISIONS[4] or self.current_condition == Enemy.CONDISIONS[1]:
            b =  self.input_texter.return_my_text()
            if self.str_text_for_question ==b:
                self.die()
            
       
    def define_current_condition(self):
        if  self.current_condition !=self.CONDISIONS[3]:
            if self.find_actual_dist() < self.attack_distance:
                self.current_condition = Enemy.CONDISIONS[1]
            elif self.find_actual_dist() < self.battle_distance:
                self.current_condition = Enemy.CONDISIONS[4]
                if self.previous_condition != self.current_condition:
                    self.enter_in_battle(self.str_text_for_question)
                    self.animation_updater = self.animation_updater*4
                
            elif self.find_actual_dist() < self.launch_distance:
                self.current_condition = Enemy.CONDISIONS[2]
                if self.previous_condition ==  Enemy.CONDISIONS[4]:
                    self.question_texter.write_text('')
                    self.input_texter.write_text('')
                    self.input_texter.inWork = True
            
            else:
                self.current_condition = Enemy.CONDISIONS[0]
            self.previous_condition = self.current_condition
         
    def attack(self, player):
        self.ticker += 1
        if self.ticker > 100:
            self.ticker = 0
            if  player.health -  self.damage <0:
                player.health = 0
            else:
                player.health -= self.damage

    def set_texters(self, input_text_obj, question_text_obj):
        self.input_texter =input_text_obj
        self.question_texter = question_text_obj
        self.input_texter.hide(True)
        self.question_texter.hide(True)
    def die(self):
        super().die()
        self.animation_left[0] = scenes.Movable_Game_Object.die_image
        self.animation_right[0] =scenes.Movable_Game_Object.die_image
        self.player.we_kill_enemy()
        self.current_condition = Enemy.CONDISIONS[3]
        self.question_texter.write_text('')
        self.input_texter.write_text('')
        self.player.inbattle = False
        self.input_texter.inWork = False
        self.input_texter.hide(True)
        self.question_texter.hide(True)
    def enter_in_battle(self,text):
        self.input_texter.hide(False)
        self.question_texter.hide(False)
        self.question_texter.write_text(text)
        self.player.inbattle = True
        self.input_texter.inWork = True
        self.speed = self.speed * 0.05


        

    