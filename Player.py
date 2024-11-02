class Player():
    def __init__(self):
        self.bankPieces = 9
        self.playerPieces = 9

    def bankUpdate(self):
        self.bankPieces -= 1

    def getBankPieces(self):
        return self.bankPieces

    def pieceUpdate(self):
        self.playerPieces -= 1

    def getPlayerPieces(self):
        return self.playerPieces

