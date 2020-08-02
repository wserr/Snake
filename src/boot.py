from snake.Main import Game
from odroid_go import GO
from IntroScreen import IntroScreen
from GameOverScreen import GameOverScreen
from NewHighScoreScreen import NewHighScoreScreen
from HighScoreScreen import HighScoreScreen

if (GO.btn_menu.is_pressed()==1):
    score = Game.Play(10)