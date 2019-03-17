from odroid_go import GO
import Main
import machine
import time

class WelcomeScreen():
    def __init__(self):
        GO.lcd.set_font(GO.lcd.fonts.TT24)
        GO.lcd.erase()
        GO.lcd.set_pos(0, 0)
        GO.lcd.print("Welcome! Press A to start playing...")
        ack = False
        while(not ack):
            GO.update()
            ack = GO.btn_a.is_pressed() == 1
            time.sleep(0.5)
        game = Main.Game()
        