import btree
import ujson

class Database:
    AmountOfHighScores = 5

    def Open(self):
        newDb = False
        try:
            f = open("mydb", "r+b")
        except OSError:
            f = open("mydb", "w+b")
            newDb = True
        self.DB = btree.open(f)
        self.File = f

        if(newDb==True):
            self.PlayerList = []
            self.DB[b"1"] = ujson.dumps(self.PlayerList)
            self.DB.flush()
        else:
            self.PlayerList = ujson.loads(self.DB[b"1"])


    def Close(self):
        self.DB.close()
        self.File.close()

    def Save(self):
        self.DB[b"1"] = ujson.dumps(self.PlayerList)


    def GetAllPlayers(self):
        #haal alle spelers + scores op
        #1: FLO with 29 points
        #2: WIS with 28 points
        #3: HAR with 27 points
        result = []
        index = 1
        for player in self.PlayerList:
            split = player.split(";")
            result.append(str(index) +": " + split[0] + ": " + split[1] + " points")
            index = index+1
        return result
    

    def IsHighScore(self, score):
        amount = len(self.PlayerList)
        if (amount<self.AmountOfHighScores):
            return True
        else:
            lowestScore = int(self.PlayerList[amount-1].split(";")[1])
            return score > lowestScore

    def InsertHighScore(self, score, name):
        #add high score to DB
        indexToInsert = 0
        for player in self.PlayerList:
            playerScore =  int(player.split(";")[1])
            if(score<=playerScore):
                indexToInsert = indexToInsert + 1
        self.PlayerList.insert(indexToInsert,name+";"+str(score))
        if(len(self.PlayerList)>self.AmountOfHighScores):
            self.PlayerList.pop(len(self.PlayerList)-1)
        self.Save()

            

    





        