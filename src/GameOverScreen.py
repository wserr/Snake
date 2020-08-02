import time
from odroid_go import GO

class GameOverScreen:
    def Show(self,score):
        self.Score = score
        self.Initialize()
        self.ButtonLoop()

    def ButtonLoop(self):
        pause = True
        while (pause==True):
            GO.update()
            pause = not GO.btn_a.is_pressed()
            
    def Initialize(self):
        GO.lcd.erase()
        GO.lcd.set_color(fg=GO.lcd.colors.WHITE, bg=GO.lcd.colors.BLACK)
        GO.lcd.set_font(GO.lcd.fonts.TT32)
        GO.lcd.set_pos(0,0)
        GO.lcd.print("Game Over")
        GO.lcd.print("Score: " + str(self.Score))
        GO.lcd.print("Press A to continue")
