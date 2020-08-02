from odroid_go import GO
from snake.Entities import Globals
from snake.Entities import Block
import time

#Options
#1=Play
#2=High Scores

class IntroScreen:
    def Show(self):
        self.Initialize()
        return self.ButtonLoop()

    def ButtonLoop(self):
        pause = True
        while (pause==True):
            GO.update()
            pause = not GO.btn_a.is_pressed()
            if(GO.btn_joy_y.is_axis_pressed() == 2 or GO.btn_joy_y.is_axis_pressed() == 1):
                #Up or down
                self.ToggleSelection()
                time.sleep(0.1)
        return self.SelectedOption

    def ToggleSelection(self):
        if(self.SelectedOption==1):
            self.SelectedOption=2
        elif(self.SelectedOption==2):
            self.SelectedOption=1
        self.UpdateSelectedOption()

    def Initialize(self):
        GO.lcd.erase()
        GO.lcd.set_color(fg=GO.lcd.colors.WHITE, bg=GO.lcd.colors.BLACK)
        GO.lcd.set_font(GO.lcd.fonts.TT32)
        GO.lcd.set_pos(0,0)
        GO.lcd.print("Snake")
        GO.lcd.set_pos(30,70)
        GO.lcd.print("Play")
        GO.lcd.print("High Scores")

        self.Selection1 = Block.Block(10,80,10,10)
        self.Selection2 = Block.Block(10,110,10,10)
        self.SelectedOption = 1
        self.UpdateSelectedOption()

    def UpdateSelectedOption(self):
        if(self.SelectedOption==1):
            self.SetFirstOption()
        elif(self.SelectedOption==2):
            self.SetSecondOption()

    def SetFirstOption(self):
        Globals.FillRectangle(self.Selection1,GO.lcd.colors.GREEN)
        Globals.FillRectangle(self.Selection2,GO.lcd.colors.BLACK)

    def SetSecondOption(self):
        Globals.FillRectangle(self.Selection1,GO.lcd.colors.BLACK)
        Globals.FillRectangle(self.Selection2,GO.lcd.colors.GREEN)



    