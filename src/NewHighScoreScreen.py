from odroid_go import GO
from snake.Entities import Globals
from snake.Entities import Block
import time


class NewHighScoreScreen:
    MinSelection = 1
    MaxSelection = 3
    SelectedOption = 1
    Text = "AAA"
    InitialPosition = [0,0]
    NamePosition = [30,70]
    SelectionBlockSize = 10

    def Show(self):
        self.Initialize()
        return self.ButtonLoop()
        
    def ButtonLoop(self):
        pause = True
        while (pause==True):
            GO.update()
            pause = not (GO.btn_a.is_pressed())
            if(GO.btn_joy_x.is_axis_pressed() == 2): 
                #left
                self.DecreaseSelection()

            elif(GO.btn_joy_x.is_axis_pressed() == 1):
                #right
                self.IncreaseSelection()

            elif(GO.btn_joy_y.is_axis_pressed() == 2):
                #up
                self.Text = self.ReplaceCharacterInString(self.Text,self.SelectedOption-1,self.GetPreviousLetter(self.Text[self.SelectedOption-1]))
                self.UpdateText()
            elif(GO.btn_joy_y.is_axis_pressed() == 1):
                #down
                self.Text = self.ReplaceCharacterInString(self.Text,self.SelectedOption-1,self.GetNextLetter(self.Text[self.SelectedOption-1]))
                self.UpdateText()

            time.sleep(0.1)
        return self.Text

    def ReplaceCharacterInString(self,text,index,newChar):
        old = text
        stringList = list(old)
        stringList[index] = newChar
        return "".join(stringList)

    def IncreaseSelection(self):
        self.SelectedOption = self.SelectedOption+1
        if(self.SelectedOption>self.MaxSelection):
            self.SelectedOption=self.MinSelection
        self.UpdateSelectedOption()

    def DecreaseSelection(self):
        self.SelectedOption = self.SelectedOption-1
        if(self.SelectedOption<self.MinSelection):
            self.SelectedOption = self.MaxSelection
        self.UpdateSelectedOption()

    def Initialize(self):
        GO.lcd.erase()
        GO.lcd.set_color(fg=GO.lcd.colors.WHITE, bg=GO.lcd.colors.BLACK)
        GO.lcd.set_font(GO.lcd.fonts.TT32)
        GO.lcd.set_pos(self.InitialPosition[0],self.InitialPosition[1])
        GO.lcd.print("New Highscore!")
        GO.lcd.set_font(GO.lcd.fonts.TT14)
        GO.lcd.print("Enter name and press A")
        GO.lcd.set_font(GO.lcd.fonts.TT32)

        self.Selection1 = Block.Block(self.NamePosition[0]+2,self.NamePosition[1]+30,self.SelectionBlockSize,self.SelectionBlockSize)
        self.Selection2 = Block.Block(self.NamePosition[0]+22,self.NamePosition[1]+30,self.SelectionBlockSize,self.SelectionBlockSize)
        self.Selection3 = Block.Block(self.NamePosition[0]+42,self.NamePosition[1]+30,self.SelectionBlockSize,self.SelectionBlockSize)
        self.Selection4 = Block.Block(self.NamePosition[0]+62,self.NamePosition[1]+30,self.SelectionBlockSize,self.SelectionBlockSize)
        self.UpdateText()
        self.UpdateSelectedOption()
        
    def UpdateSelectedOption(self):
        if(self.SelectedOption==1):
            self.SetFirstOption()
        elif(self.SelectedOption==2):
            self.SetSecondOption()
        elif(self.SelectedOption==3):
            self.SetThirdOption()

    def SetFirstOption(self):
        Globals.FillRectangle(self.Selection1,GO.lcd.colors.GREEN)
        Globals.FillRectangle(self.Selection2,GO.lcd.colors.BLACK)
        Globals.FillRectangle(self.Selection3,GO.lcd.colors.BLACK)

    def SetSecondOption(self):
        Globals.FillRectangle(self.Selection1,GO.lcd.colors.BLACK)
        Globals.FillRectangle(self.Selection2,GO.lcd.colors.GREEN)
        Globals.FillRectangle(self.Selection3,GO.lcd.colors.BLACK)

    def SetThirdOption(self):
        Globals.FillRectangle(self.Selection1,GO.lcd.colors.BLACK)
        Globals.FillRectangle(self.Selection2,GO.lcd.colors.BLACK)
        Globals.FillRectangle(self.Selection3,GO.lcd.colors.GREEN)


    def GetNextLetter(self, currentLetter):
        currentIndex = Globals.ALPHABET.index(currentLetter)
        currentIndex = currentIndex + 1
        if(currentIndex == Globals.ALPHABET_COUNT):
            currentIndex=0
        return Globals.ALPHABET[currentIndex]

    def GetPreviousLetter(self, currentLetter):
        currentIndex = Globals.ALPHABET.index(currentLetter)
        currentIndex = currentIndex - 1
        if(currentIndex == -1):
            currentIndex=Globals.ALPHABET_COUNT-1
        return Globals.ALPHABET[currentIndex]

    def UpdateText(self):
        GO.lcd.set_pos(self.NamePosition[0],self.NamePosition[1])
        GO.lcd.print(self.Text)