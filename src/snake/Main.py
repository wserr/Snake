from odroid_go import GO
import machine
import time
from .Entities import PlayField
from .Entities import Snake
from .Entities import Globals
from .InputTexts import *


class Main():
  def Play(self, maxScore):
    GO.lcd.erase()
    GO.lcd.fill(color=GO.lcd.colors.BLACK)
    GO.lcd.set_font(GO.lcd.fonts.TT14)
    GO.lcd.set_color(fg=GO.lcd.colors.WHITE, bg=GO.lcd.colors.BLACK)
    self.playField = PlayField.PlayField()
    self.Snake = Snake.Snake(Globals.SNAKEINIT_X,Globals.SNAKEINIT_Y,Globals.INITIALDIRECTION)
    self.playField.GetNewFoodBlock(self.Snake)
    self.MaxScore = maxScore

    Globals.FillRectangles(self.Snake.Body,Globals.SNAKE_COLOR)
    self.TimersActive = False
    
    self.Score = 0
    GO.speaker.set_volume(10)
    UpdateScore(self.Score)
    #UpdateBattery()

    #self.BatteryUpdateTimer = machine.Timer(1)

    #self.BatteryUpdateTimer.init(period=5000, mode=machine.Timer.PERIODIC, callback=self.UpdateBattery)
    self.InternalCounter = 0

    self.TimersActive = True

    self.Playing = True
    while self.Playing:
      self.UpdateInput()
      time.sleep(0.0001)
    GO.lcd.erase()
    return self.Score

  def UpdateBattery(self,timer):
    UpdateBattery()

  def StopTimers(self):
      self.TimersActive = False
      #self.BatteryUpdateTimer.deinit()

  def UpdateInput(self):
    GO.update()
    self.InternalCounter = self.InternalCounter+1
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
    if self.InternalCounter == 4:
      self.InternalCounter = 0
      self.UpdateScreen()
      
  def UpdateScreen(self):
      self.Snake.Move()
      Globals.DrawSnake(self.Snake)
      if self.playField.DetectCollisionWithWalls(self.Snake.Head) or self.playField.DetectCollisionWithItSelf(self.Snake):
        self.StopTimers()
        self.Playing = False
        Globals.LostTone()
      if self.playField.DetectCollisionWithFood(self.Snake.Head):
        self.Snake.AddBlock()
        self.playField.GetNewFoodBlock(self.Snake)
        self.Score = self.Score + 1
        UpdateScore(self.Score)
        Globals.FoodTone()
      if(self.Score==self.MaxScore):
        self.Playing = False
        Globals.WinTone()

Game = Main()


        