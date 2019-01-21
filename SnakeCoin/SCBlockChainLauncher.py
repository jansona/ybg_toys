from SnakeCoinBlockChain import SCBlockChain


if __name__ == "__main__":
    blockChain = SCBlockChain()
    for i in range(1,10):
        blockChain.generateCoin()
    blockChain.checkAll()