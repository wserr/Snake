
class Block():
    def __init__(self,x,y,width,length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    def __str__(self):
        return str(self.x) + ' , ' + str(self.y)

def CopyTo(block):
    return Block(block.x,block.y,block.width,block.length)

def CopyToExistingBlock(block1,block2):
    block2.x = block1.x
    block2.y = block1.y
    block2.width = block1.width
    block2.length = block1.length
    return block2

def CheckEqual(block1,block2):
    if block1.x == block2.x and block1.y == block2.y and block1.length == block2.length and block1.width == block2.width:
        return True
    else:
        return False

