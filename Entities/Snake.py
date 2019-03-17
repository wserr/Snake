from odroid_go import GO
from Entities.Block import Block,CopyTo,CopyToExistingBlock
from Entities import Globals

class Snake():
    def __init__(self,initX,initY,initDirection):
        self.Body = []
        
        self.DirectionChanged = False
        
        #Initialize body with one block
        self.Body.append(Block(initX + Globals.INIT_X + Globals.SNAKEINIT_X,initY + Globals.INIT_Y+Globals.SNAKEINIT_Y,Globals.BLOCK_SIZE,Globals.BLOCK_SIZE))
        self.Body.append(Block(initX + Globals.INIT_X + Globals.SNAKEINIT_X - 10,initY + Globals.INIT_Y+Globals.SNAKEINIT_Y,Globals.BLOCK_SIZE,Globals.BLOCK_SIZE)) 
        self.Body.append(Block(initX + Globals.INIT_X + Globals.SNAKEINIT_X - 20,initY + Globals.INIT_Y+Globals.SNAKEINIT_Y,Globals.BLOCK_SIZE,Globals.BLOCK_SIZE))   
        self.Head = self.Body[0]
        self.Tail = None
        self.BlockBehindTail = None
        self.Direction = initDirection
        self.FoodEaten = False

    def SetDirection(self, direction):
        if self.Direction != direction:
            if self.Direction == 1 and not direction == 2:
                self.DirectionChanged = True
                self.Direction = direction
            elif self.Direction == 2 and not direction == 1:
                self.DirectionChanged = True
                self.Direction = direction
            elif self.Direction == 3 and not direction == 4:
                self.DirectionChanged = True
                self.Direction = direction
            elif self.Direction == 4 and not direction == 3:
                self.DirectionChanged = True
                self.Direction = direction

    def GetDirection(self):
        self.DirectionChanged = False
        return self.Direction

    def Move(self):
        self.BlockBehindTail = CopyTo(self.Body[len(self.Body)-1])
        #Move rest of the snake
        for x in range(len(self.Body)-1,0,-1):
            self.Body[x] = CopyToExistingBlock(self.Body[x-1],self.Body[x])
        if self.Direction == 1:
            #Forward
            self.Head.y = self.Head.y - Globals.BLOCK_SIZE
        elif self.Direction == 2:
            #Backward
            self.Head.y = self.Head.y + Globals.BLOCK_SIZE
        elif self.Direction == 3:
            #Left
            self.Head.x = self.Head.x - Globals.BLOCK_SIZE
        elif self.Direction == 4:
            #Right
            self.Head.x = self.Head.x + Globals.BLOCK_SIZE
        if self.FoodEaten:
            self.Body.append(self.BlockBehindTail)
            self.FoodEaten = False
            self.BlockBehindTail = None      

    def AddBlock(self):
        self.FoodEaten = True