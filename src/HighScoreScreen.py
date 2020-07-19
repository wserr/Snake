from odroid_go import GO
import Main
import machine
import time

class HighScoreScreen():
    def __init__(self, highScore):
        GO.lcd.set_font(GO.lcd.fonts.TT24)
        GO.lcd.erase()
        GO.lcd.set_pos(0, 0)
        GO.lcd.print("Your Score was: " + highScore ". Great Job!")
        GO.lcd.set_pos(10, 0)
        GO.lcd.print("Press A to restart, and B to quit")
        ack = False
        while(not ack):
            GO.update()
            ack = GO.btn_a.is_pressed() == 1
            time.sleep(0.1)
