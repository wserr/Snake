from . import Globals
from .Block import Block, CheckEqual
from odroid_go import GO
import random

#Directions
#1: Forward
#2: Backward
#3: Left
#4: Right

class PlayField():
    def __init__(self):
        self.Width = Globals.SCREEN_WIDTH - Globals.INIT_X
        self.Height = Globals.SCREEN_HEIGHT - Globals.INIT_Y
        self.PlayableArea = Block(Globals.INIT_X+Globals.BLOCK_SIZE,Globals.INIT_Y+Globals.BLOCK_SIZE,Globals.INIT_X + self.Width-2*Globals.BLOCK_SIZE, Globals.INIT_Y + self.Height-2*Globals.BLOCK_SIZE)
        self.DrawBorders()
        
    def GetNewFoodBlock(self,snake):
        potentialBlock = self.GetPotentialBlock()
        while(self.DetectIfFoodBlockWithinSnake(snake,potentialBlock)):
            potentialBlock = self.GetPotentialBlock()
        self.Food = potentialBlock
        Globals.FillRectangle(self.Food,Globals.FOOD_COLOR)

    def GetPotentialBlock(self):
        x = int(random.randint(self.PlayableArea.x, self.PlayableArea.width)/Globals.BLOCK_SIZE) * Globals.BLOCK_SIZE
        y = int(random.randint(self.PlayableArea.y, self.PlayableArea.length)/Globals.BLOCK_SIZE) * Globals.BLOCK_SIZE
        return  Block(x,y,Globals.BLOCK_SIZE,Globals.BLOCK_SIZE)


    def DetectCollisionWithItSelf(self,snake):
        for i in range(1,len(snake.Body)):
            if CheckEqual(snake.Body[i],snake.Head):
                return True
        return False

    def DetectIfFoodBlockWithinSnake(self, snake, foodBlock):
        for i in range(1,len(snake.Body)):
            if CheckEqual(snake.Body[i],foodBlock):
                return True
        return False   
        

    def DetectCollisionWithFood(self, head):
        if head.x == self.Food.x and head.y == self.Food.y:
            return True
        else:
            return False

    def DetectCollisionWithWalls(self,head):
        if self.PlayableArea.x <= head.x and self.PlayableArea.width >= head.x and self.PlayableArea.y <= head.y and self.PlayableArea.length >= head.y:
            return False
        else:
            return True

    def DrawBorders(self):
        blocks = []
        #Line Above
        blocks.append(Block(Globals.INIT_X,Globals.INIT_Y,self.Width,Globals.BLOCK_SIZE))

        #Line Right
        blocks.append(Block(Globals.INIT_X + self.Width-Globals.BLOCK_SIZE,Globals.INIT_Y,Globals.BLOCK_SIZE,self.Height))

        #Line Bottom
        blocks.append(Block(Globals.INIT_X,self.Height+Globals.INIT_Y-Globals.BLOCK_SIZE,self.Width,Globals.BLOCK_SIZE))

        #Line Left
        blocks.append(Block(Globals.INIT_X,Globals.INIT_Y,Globals.BLOCK_SIZE,self.Height))

        #Draw All
        Globals.FillRectangles(blocks,Globals.BORDER_COLOR)

        