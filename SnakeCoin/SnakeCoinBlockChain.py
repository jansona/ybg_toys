import datetime as date
from SnakeCoinBlock import Block
from SnakeCoinGenesis import createGenesisBlock


class SCBlockChain(object):
    def __init__(self):
        self.chainList = []
        self.chainList.append(createGenesisBlock())

    def generateCoin(self):
        lastCoin = self.chainList[-1]
        newIndex = lastCoin.index + 1
        newTimestamp = date.datetime.now()
        newData = "Hey! I'm the block " + str(newIndex)
        previousHash = lastCoin.hash
        self.chainList.append(Block(newIndex, newTimestamp, newData, previousHash))

    def checkAll(self):
        for block in self.chainList:
            print("Block #{} at {} with data: {}\nHash: {}\n\n"
            .format(block.index, block.timestamp, block.data, block.hash))
