import scenes, pygame, math
class Enemy(scenes.Movable_Game_Object):
    CONDISIONS = ('stay','attack','chase','die')#У противника есть разные состояния, но текущим может быть только одно
    def __init__(self, surface, cords, player_Obj) -> None:
        super().__init__(surface, cords)
        self.player = player_Obj
        self.launch_distance = 400 #дистанция, с которой противник начинает преследовать игрока(условно - это половина ребра квадрата)
        self.attack_distance = 100 #дистанция, с которой начинается бой с противником
        self.current_condition = Enemy.CONDISIONS[0]
        self.speed = 0.3
    def find_actual_dist(self):
        self.xdist = self.player.cords[0] - self.cords[0]
        self.ydist = self.player.cords[1] - self.cords[1]
        actual_distance = (self.xdist**2 + self.ydist**2)**(1/2)
        return actual_distance
    def update(self):
        super().update()
        self.define_current_condition()
        if self.current_condition == Enemy.CONDISIONS[2]:
            actual_distance = self.find_actual_dist()
            self.speed_vector = [self.xdist/actual_distance* self.speed, self.ydist/actual_distance*self.speed ]
        else:
            self.speed_vector = [0,0]
       
    def define_current_condition(self):
         if self.find_actual_dist() < self.launch_distance:
             self.current_condition = Enemy.CONDISIONS[2]
         else:
             self.current_condition = Enemy.CONDISIONS[0]
        


        

    