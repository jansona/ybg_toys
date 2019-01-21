import hashlib as hasher

class Block(object):
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashBlock()

    def hashBlock(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) + 
                   str(self.data) +
                   str(self.previous_hash)).encode("utf8"))
        return sha.hexdigest()

        