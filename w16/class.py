import random

class Player():
    def __init__(self, name):
        self.name = name
        self.guesses = []
        self.choice = ""
        self.winner = False

    def checkGuess(self, other):
        if other.choice in self.guesses:
             print("hit")
             self.winner = True
        else:
             print("miss")

    def isWinner(self):
         return self.winner 

class Human(Player):
    def getChoice(self):
        print('\nGive me a number between 1 to 20')
        try:
            self.choice = int(input())

            while self.choice > 20:
                print('You should give a number between 0 to 20. Please try '
                    'again.')
                self.choice = int(input())
        except:

            print('Hmmm! Something going wrong. You must enter a valid '
                'number here.')
            print("Let's begin the game again!\n")
            self.getChoice()

    def getGuess(self):
        try:
            print("\nIt's your turn, take a guess")
            g = int(input())

            while g in self.guesses or g not in range(1, 21):
                if g in self.guesses:
                    print('You guessed that number already. Please enter '
                          'another number.')
                    print('Here are the number you have used already: ' +
                          str(self.guesses))
                elif g not in range(1, 21):
                    print('You must eneter a number between 1 and 20. Please '
                          'enter another number.')
                print('\nTake a guess')
                g = int(input())

            self.guesses.append(g)
            print('You guessed ' + str(g))
        except ValueError:
            print('Ooops! You must enter a number as your guess. Lets try '
                  'this again.')
            self.getGuess()    

class Computer(Player):
    def getChoice(self):
        self.choice = random.randint(1, 20)
        print('\nThe computer has chosen a number as well')

    def getGuess(self):
        print("\nIt's computer's turn")

        g = random.choice(list(range(1,21)))

        while g in self.guesses:
            g = random.choice(list(range(1,21)))
        
        self.guesses.append(g)
        print('Computer guessed ' + str(g))


p1 = Human("Dumi")
print(p1.name)
print(p1.guesses)
print(p1.choice)
print(p1.winner)

p2 = Computer("Dan")
print(p2.name)
print(p2.guesses)
print(p2.choice)
print(p2.winner)

""" p1.getChoice()
p1.getGuess()
print("--------------------")
print(p1.choice)
print("--------------------")
print(p1.guesses)

p2.getChoice()
p2.getGuess()
print("--------------------")
print(p2.choice)
print("--------------------")
print(p2.guesses)

p1.checkGuess(p2)
 """

#have both p1 and p2 select their choices
p1.getChoice()
p2.getChoice()

""" print("P1 Choice: ", p1.choice)
print("P2 Choice: ", p2.choice) """

while not(p1.isWinner() or p2.isWinner()):
    #p1 guesses first
    p1.getGuess()
    p1.checkGuess(p2)

    #if p1 won no need to ask p2 to guess - break out of loop
    if p1.isWinner():
        break

    #p2 guessed second
    p2.getGuess()
    p2.checkGuess(p1)
    #no need to break here - end of loop

if p1.isWinner():
    print(f"\nCongratulations {p1.name}! You Won!")
elif p2.isWinner():
    print(f"\nCongratulations {p2.name}! You Won!")