from snake.Main import Game
from odroid_go import GO

if (GO.btn_menu.is_pressed()==1):
    score = Game.Play(10)