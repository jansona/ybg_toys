import datetime
import SnakeCoinBlock

def createGenesisBlock():
    # 手动添加区块链的第一个块
    # 设其下标为0，前一个块（previous block）的哈希值为"0"
    return SnakeCoinBlock.Block(0, datetime.datetime.now(), "GenesisBlock", "0")