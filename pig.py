import random

class Pig:
    def __init__(self, roll, winner):
        self.roll = [random.randint(1, 6) , 'hold']
        self.winner = sum(random.radint(1,6) >= 100)

    def Player1Turn(self, roll):
        if self.roll == 1 or 'hold':
            pass
        if self.roll == 2-6:
            self.winner
    def Player2Turn(self, roll):
        if self.roll == 1 or 'hold':
            pass
        if self.roll == 2-6:
            self.winner

    def winner(self, winner):
        if Player1Turn() >= 100 <= Player2Turn():
            print ('Player 1 Wins')
        if Player2Turn >= 100 <= Player1Turn():
            print ('Player 2 Wins')

Winner = Pig(roll, winner)

Winner.winner()

exit(Pig)

if __name__ == "__main__":
    pass
    
