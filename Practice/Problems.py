import inspect 
from decimal import Decimal, Context, setcontext
class Console_Utility:
    
    def Header(self, title = ""):

        if title != "":
            print()
            print()
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{title.ljust(60, ' ').rjust(65, ' ').ljust(80, '-').rjust(100, '-')}>")
            print(f'{'<'.ljust(101, '_')}>')
        else:
            print()
            print()
            caller_frame = inspect.stack()[1]
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{caller_frame.function.ljust(60, ' ').rjust(65, ' ').ljust(80, '-').rjust(100, '-')}>")
            print(f'{'<'.ljust(101, '_')}>')
            
 
class Problems:

    Util = Console_Utility()

    def Fibonacci(self, number):
        '''fibonacci sequence has two starting seeds 0 and 1 or 1 and 1
        each number is given a position like an index
        the most recent two numbers are added together to make the next number '''

        self.Util.Header()
        
        # instantiate the list with zeros at the size of the sequence n + 1
        fib = [0] * number
        fib[1] = 1
        for index in range(2, number):

            fib[index] = fib[index - 1] + fib[index - 2]
            # print(f'index: {index}  n: {n}')
        print(fib)
    
    def Fizz_Buzz(self, number):
        '''iterate through each number from 0 up through the injected number
        Print fizz if a number is divisible by 3
        print buzz if a number is divisible by 5
        print fizzbuzz if a number is divisible by 3 and 5'''

        self.Util.Header()
        result = ''
        for index in range(0, number + 1):
            match index:
                case index if (index % 3 == 0) and (index % 5 == 0):
                    result += "fizzbuzz"
                case index if index % 3 == 0:
                    result += "fizz"
                case index if index % 5 == 0:
                    result += "buzz"
                case _:
                    result += "..."
            result += '\n'
        return result


    def isPalindromeNumber(self, number: int):
        '''take in a max number
        iterate over every number through that number
        check if they are palindromes'''
        self.Util.Header()

        palindrome = []
        for item in range(0, number + 1):

            if str(item)[::-1] == str(item):
                palindrome.append(item)
        
        return palindrome
    
    def RockPaperScissors(self):
        self.Util.Header()
        import random

        is_playing = True # unnecessary if you use the quit option
        while is_playing == True:
        # while True: # use this if you use the quit option mentioned later
            player1 = input('Select Rock, Paper, or Scissors: ').lower()
            player2 = random.choice(['Rock', 'Paper', 'Scissors']).lower()
            print('Player 2 selected', player2)

            if player1 == 'rock' and player2 == 'paper':
                print('Player 2 Wins!')
            elif player1 == 'paper' and player2 == 'scissors':
                print('Player 2 Wins!')
            elif player1 == 'scissors' and player2 == 'rock':
                print('Player 2 Wins!')
            elif player1 == player2:
                print('Tie!')
            else:
                print('Player 1 Wins!')
            
            replay = input('Do you want to play again? (input y/n)')
            if replay == 'n':
                print('The user chose to stop playing Rock, Paper, Scissors')
                is_playing = False
                # quit() # optionally you could just quit here instead of changing the condition

            else: # the else isn't necessary here but makes the code clear.
                continue
    
    def Pi_Innaccurate(self, terms = 1000000):
        '''Calculate Pi using the Nalinkantha series'''
        self.Util.Header()

        setcontext(Context(prec = terms))
        pi = Decimal(3)
        sign = 1
        number = 2
        
        while number < terms:
            pi += Decimal((sign * 4) / (number * (number + 1) * (number + 2)))
            sign *= -1
            number += 2

        return pi
    
    def Eulers_Number(self, terms = 10000):
        '''Euler's number calculated as The infinite series 1 + 1/1! + 1/2! + 1/3! + ...
          can be used to calculate e. 
        Each term in the series represents a factorial 
        (the product of all positive integers up to that number). 
        For instance, 1! = 1, 2! = 2 * 1 = 2, 3! = 3 * 2 * 1 = 6, and so on. '''
        self.Util.Header()

        euler = 2
        factorial = [1]
        for index in range(1, terms):
            factorial.append(factorial[index - 1] * (index + 1))
            euler += 1 / factorial[index]

        return euler       