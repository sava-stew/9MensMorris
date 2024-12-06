class Player():
    def __init__(self):
        self.bankPieces = 6
        self.playerPieces = 6

    def setPieces(self, num):
        self.bankPieces = num
        self.playerPieces = num

    def bankUpdate(self):
        self.bankPieces -= 1

    def getBankPieces(self):
        return self.bankPieces

    def pieceUpdate(self):
        self.playerPieces -= 1

    def getPlayerPieces(self):
        return self.playerPieces

