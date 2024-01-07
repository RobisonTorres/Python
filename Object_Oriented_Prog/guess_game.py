print('Object Oriented Programming.')
print()

class Guesser:
    """"
    Imagine you are creating a game where the user has to guess the correct number.
    But there is a limit of how many guesses the user can do.
    (...)
    """
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):

        if self.lives == 0:
            raise Exception('Omae wa mo shindeiru')
        elif n == self.number:
            return True
        else:
            self.lives -= 1
            return False        

game = Guesser(3, 2)
print(game.guess(1))  # Outputs - False
print(game.guess(3))  # Outputs - True