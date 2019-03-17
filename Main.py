from odroid_go import GO
import machine
import time
from Entities import PlayField
from Entities import Snake
from Entities import Globals
from InputTexts import *
import WelcomeScreen

class Game():
  def __init__(self):
    GO.lcd.erase()
    GO.lcd.set_font(GO.lcd.fonts.TT14)
    self.playField = PlayField.PlayField()
    self.Snake = Snake.Snake(Globals.SNAKEINIT_X,Globals.SNAKEINIT_Y,Globals.INITIALDIRECTION)
    Globals.FillRectangles(self.Snake.Body,Globals.SNAKE_COLOR)
    self.TimersActive = False
    
    self.Score = 0
    UpdateScore(self.Score)
    UpdateBattery()
    self.InputTimer = machine.Timer(2)
    self.ScreenUpdateTimer = machine.Timer(0)
    self.BatteryUpdateTimer = machine.Timer(1)

    self.InputTimer.init(period=10, mode=machine.Timer.PERIODIC, callback=self.UpdateInput)
    self.ScreenUpdateTimer.init(period=100, mode=machine.Timer.PERIODIC, callback=self.UpdateScreen)
    self.BatteryUpdateTimer.init(period=5000, mode=machine.Timer.PERIODIC, callback=self.UpdateBattery)

    self.TimersActive = True

    self.Playing = True
    while self.Playing:
      time.sleep(0.01)

  def UpdateBattery(self,timer):
    UpdateBattery()

  def StopTimers(self):
      self.TimersActive = False
      self.InputTimer.deinit()
      self.ScreenUpdateTimer.deinit()

  def UpdateInput(self,timer):
    GO.update()
    if GO.btn_menu.is_pressed() == 1:
      self.StopTimers()
    else:
      if GO.btn_joy_y.is_axis_pressed() == 2:
        #Up
        self.Snake.SetDirection(1)
      elif GO.btn_joy_y.is_axis_pressed() == 1:
        #Down
        self.Snake.SetDirection(2)
      elif GO.btn_joy_x.is_axis_pressed() == 2:
        #Left
        self.Snake.SetDirection(3)
      elif GO.btn_joy_x.is_axis_pressed() == 1:
        #Right
        self.Snake.SetDirection(4)
      

  def UpdateScreen(self,timer):
      self.Snake.Move()
      Globals.DrawSnake(self.Snake)
      if self.playField.DetectCollisionWithWalls(self.Snake.Head) or self.playField.DetectCollisionWithItSelf(self.Snake):
        self.StopTimers()
        self.Playing = False
      if self.playField.DetectCollisionWithFood(self.Snake.Head):
        self.Snake.AddBlock()
        self.playField.GetNewFoodBlock()
        self.Score = self.Score + 1
        UpdateScore(self.Score)



        