from snake.Main import Game
from snake.Entities import Globals
from snake.Entities import Block
from odroid_go import GO
import sys
import time

def PauseUntilAPressed():
    pause = True
    while (pause == True):
        GO.update()
        pause = not GO.btn_a.is_pressed()
        if (GO.btn_menu.is_pressed()):
            sys.exit()
        time.sleep(0.1)

def IntroMessage():
    GO.lcd.erase()
    GO.lcd.fill(color=GO.lcd.colors.BLACK)
    GO.lcd.set_font(GO.lcd.fonts.TT32)
    GO.lcd.print("Gelukkige verjaardag Elles!!")
    GO.lcd.print("Opdracht:")
    GO.lcd.print("Haal meer dan 10 punten in snake")
    GO.lcd.print("Druk op A om te beginnen...")
    PauseUntilAPressed()

def SuccessMessage():
    GO.lcd.erase()
    GO.lcd.fill(color=GO.lcd.colors.BLACK)
    GO.lcd.set_font(GO.lcd.fonts.TT32)
    GO.lcd.set_color(fg=GO.lcd.colors.WHITE, bg=GO.lcd.colors.BLACK)
    GO.lcd.print("Het is je gelukt!!")
    GO.lcd.print("Druk op A om de hint te zien...")
    PauseUntilAPressed()

def FailMessage(score):
    GO.lcd.erase()
    GO.lcd.fill(color=GO.lcd.colors.BLACK)
    GO.lcd.set_font(GO.lcd.fonts.TT32)
    GO.lcd.set_color(fg=GO.lcd.colors.WHITE, bg=GO.lcd.colors.BLACK)
    GO.lcd.print("Mislukt :( je haalde slechts " + str(score) + " punten...")
    GO.lcd.print("Druk op A om te opnieuw te proberen...")
    PauseUntilAPressed()   

def DrawHint():
    GO.lcd.erase()
    GO.lcd.set_pos(0,0)
    GO.lcd.set_font(GO.lcd.fonts.TT32)

    GO.lcd.print("In de auto...")
    DrawCar()
    while True:
        DrawCarBody()
        time.sleep(1)
        DrawCarBody()
        DrawIndication()
        time.sleep(1)


def DrawCar():
    DrawCarBody()
    tires = []
    tires.append(Block.Block(80,40,20,45))
    tires.append(Block.Block(80,165,20,45))
    tires.append(Block.Block(190,40,20,45))
    tires.append(Block.Block(190,165,20,45)) 
    Globals.FillRectangles(tires, Globals.CAR_TIRES)

def DrawCarBody():
    carBody = Block.Block(100,50,90,150)
    Globals.FillRectangle(carBody, Globals.CAR_BODY)

    lights = []
    lights.append(Block.Block(110,40,20,10))
    lights.append(Block.Block(160,40,20,10))
    Globals.FillRectangles(lights,Globals.CAR_FRONT_LIGHTS)

def DrawIndication():
    indication = Block.Block(105,140,40,40)
    Globals.FillRectangle(indication, Globals.INDICATION)

if (GO.btn_menu.is_pressed()==1):
    IntroMessage()
    score = Game.Play(10)

    while(score<10):
        FailMessage(score)
        score = Game.Play(10)

    SuccessMessage()
    DrawHint()
