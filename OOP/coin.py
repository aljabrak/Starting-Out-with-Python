from random import *

class Coin:
    def __init__(self):
        self.sideup = 'Heads.'

    def toss(self):
        if randint(0, 1) == 0:
            self.sideup = 'Heads.'
        else:
            self.sideup = 'Tails.'

    def get_sideup(self):
        return self.sideup
    
def main():
    coin = Coin()
    print(coin.get_sideup)
    coin.toss()
    print(coin.get_sideup())

main()
