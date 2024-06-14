import enemy
import test_scene
import player
class Battle:
    def __init__(self, enemy: enemy.Enemy, quetstion_text, time) -> None:
        if enemy.current_condition == enemy.CONDISIONS[2]:
            self.quetion_text = quetstion_text


    def start(self, enemy: enemy.Enemy, player: player.Player, input_text_object:test_scene.Text_Table, quetion_text_object:test_scene.Text_Table):
        self.enemy_health = enemy.health
        self.player_health = player.health
        self.quetionText_obj =quetion_text_object
        self.inputText_obj = input_text_object
        self.quetionText_obj.write_text(self.quetstion_text)
    def update():
