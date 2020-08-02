from snake.Main import Game
from odroid_go import GO
from IntroScreen import IntroScreen
from GameOverScreen import GameOverScreen
from NewHighScoreScreen import NewHighScoreScreen
from HighScoreScreen import HighScoreScreen
from Database import Database

if (GO.btn_menu.is_pressed()==1):
    quit = False
    while not quit:
        intro = IntroScreen()
        result = intro.Show()
        if(result==1):
            score = Game.Play(50000)
            d = Database()
            d.Open()
            if(d.IsHighScore(score)):
                hs = NewHighScoreScreen()
                name = hs.Show()
                d.InsertHighScore(score,name)
                d.Close()
            else:
                GameOverScreen().Show()
        elif(result==2):
            hs = HighScoreScreen()
            hs.Show()
        elif(result==3):
            GO.lcd.erase()
            quit=True

