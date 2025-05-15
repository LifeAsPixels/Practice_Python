import inspect 
from decimal import Decimal, Context, setcontext
import numpy as np


class Console_Utility:
    
    def Header(self, title = ""):

        if title != "":
            print()
            print()
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{title.ljust(len(title) + 5, ' ').rjust(len(title) + 10, ' ').ljust(60, '-').rjust(100, '-')}>")
            print(f'{'<'.ljust(101, '_')}>')
        else:
            print()
            print()
            caller_frame = inspect.stack()[1]
            print(f'{'<'.ljust(101, '=')}>')
            print(f"<{caller_frame.function.ljust(len(caller_frame.function) + 5, ' ').rjust(len(caller_frame.function) + 10, ' ').ljust(60, '-').rjust(100, '-')}>")
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
    
    def Calculator(self):
        self.Util.Header()
        x = int(input('What is x? '))
        y = int(input('What is y? '))

        return x + y
    
    def square(self, number):
        self.Util.Header()

        return number * number
    
    def area_circle(self, radius):
        self.Util.Header()
        return 2 * np.pi * radius ** 2
    
    def Prime_Numbers(self, count):
        '''
        Return a list of some count of prime numbers
        
        >>> Problems.Prime_Numbers(10)
        [2, 3, 5, 7, 11, 13, 17, 19, 23]

        >>> Problems.Prime_Numbers(5)
        [2, 3, 5, 7]
        '''
        self.Util.Header()

        primes = [2, 3]
        number = primes[-1]
        while len(primes) < count:
            factors = False
            number += 2
            for num in range(3, number // 2):
                if number % num == 0:
                    factors = True
                    break
            if not factors:
                primes.append(number)
        while len(primes) > count:
            primes.pop()
        return primes

    def Sieve_of_Erathostenes_Prime_Set(self, limit):
        self.Util.Header()
        
        composites = []
        primes = []

        # for every number within the limit
        for number in range(2, limit + 1):
            # skip if the number is in composites
            if number in composites:
                continue
            # reset factor checking to false
            factors = False
            # check for factors in number
            for factor in range(2, number):
                if number % factor == 0:
                    factors = True
                    if number in composites:
                        break
                    else:
                        composites.append(number)
                    break
            # if a factor was found, add number to composites
            # otherwise add the number to primes
            if not factors:
                primes.append(number)
                # for every number in the range of limit divided by the prime found
                for multiple in range(2, limit // primes[-1]):
                    sieve = multiple * primes[-1]
                    # add the multiples of the prime to the composites list
                    composites.append(sieve)
        return primes
