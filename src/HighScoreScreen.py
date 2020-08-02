import time
from odroid_go import GO
from Database import Database

class HighScoreScreen:
    def Show(self):
        self.Initialize()
        self.ButtonLoop()

    def ButtonLoop(self):
        pause = True
        while (pause==True):
            GO.update()
            pause = not GO.btn_a.is_pressed()
            
    def Initialize(self):
        self.Database = Database()
        self.Database.Open()
        GO.lcd.erase()
        GO.lcd.set_color(fg=GO.lcd.colors.WHITE, bg=GO.lcd.colors.BLACK)
        GO.lcd.set_font(GO.lcd.fonts.TT32)
        GO.lcd.set_pos(0,0)
        GO.lcd.print("High Scores:")
        GO.lcd.set_font(GO.lcd.fonts.TT24)
        for player in self.Database.GetAllPlayers():
            GO.lcd.print(player)
        GO.lcd.set_font(GO.lcd.fonts.TT32)
        GO.lcd.print("Press A to continue")
        self.Database.Close()
