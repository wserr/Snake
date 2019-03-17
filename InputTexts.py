from odroid_go import GO

def PrintMessage(message):
    #GO.lcd.erase()
    GO.lcd.set_pos(0, 0)
    GO.lcd.print(message)

def UpdateBattery():
    GO.lcd.set_pos(130,0)
    GO.lcd.print("Battery: " + str(GO.battery.get_voltage()) + " V")

def UpdateScore(score):
    GO.lcd.set_pos(0, 0)
    GO.lcd.print("Score: " + str(score))    

def show_battery_voltage():
    GO.lcd.erase()
    GO.lcd.set_pos(0, 0)

    GO.lcd.print("Current Voltage: " + str(GO.battery.get_voltage()))
