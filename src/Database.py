import btree

class Database:
    def Open(self):
        try:
            f = open("mydb", "r+b")
        except OSError:
            f = open("mydb", "w+b")
        self.DB = btree.open(f)
        self.File = f

    def Close(self):
        self.DB.close()
        self.File.close()


    def GetAllPlayers(self):
        arrPlayers = []
        for player in self.DB.values():
            arrPlayers.append(player.decode("utf-8"))
        return arrPlayers

    def CheckIfHighScore(self, score):
        return True
        