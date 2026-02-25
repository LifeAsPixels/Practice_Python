import inspect 
from decimal import Decimal, Context, setcontext
import numpy as np
import time
import rich
from rich.console import Console
from rich.rule import Rule
import matplotlib.pyplot as plt

def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        # print(f"[Runtime: {elapsed:.8f}s for {func.__name__}] -> {result}")
        print(f"[Runtime: {elapsed:.8f}s for {func.__name__}]")
        return result
    return clocked                 
 
class Problems:
    console = Console()

    def func_name(self):
        caller_frame = inspect.stack()[1]
        return caller_frame.function
    
    @clock
    def Fibonacci(self, number):
        '''fibonacci sequence has two starting seeds 0 and 1 or 1 and 1
        each number is given a position like an index
        the most recent two numbers are added together to make the next number '''
        self.console.print(Rule(self.func_name()))
        
        # instantiate the list with zeros at the size of the sequence n + 1
        fib = [0] * number
        fib[1] = 1
        for index in range(2, number):

            fib[index] = fib[index - 1] + fib[index - 2]
            # print(f'index: {index}  n: {n}')
        print(fib)
    
    @clock
    def Fizz_Buzz(self, number):
        '''iterate through each number from 0 up through the injected number
        Print fizz if a number is divisible by 3
        print buzz if a number is divisible by 5
        print fizzbuzz if a number is divisible by 3 and 5
        
        this is written as mapping using an Imperative Procedure.'''

        self.console.print(Rule(self.func_name()))
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

    @clock
    @staticmethod
    def fizz_buzz_functional_map(self, number):
        '''This is fizz buzz written functionally so it can be executed as an individual call
        or many calls can be made to it using map(). compare this to the imperative procedural 
        example to see the missing for-loop that can now be optionally implemented using map()
        like this:
            number = 15
            result = "\n".join(map(get_fizz_label, range(number + 1)))
        '''
        if number % 3 == 0 and number % 5 == 0: return "fizzbuzz"
        if number % 3 == 0: return "fizz"
        if number % 5 == 0: return "buzz"
        return '...'
    
    @clock
    def isPalindromeNumber(self, number: int):
        '''take in a max number
        iterate over every number through that number
        check if they are palindromes'''
        self.console.print(Rule(self.func_name()))

        palindrome = []
        for item in range(0, number + 1):

            if str(item)[::-1] == str(item):
                palindrome.append(item)
        
        return palindrome
    
    @clock
    def RockPaperScissors(self):
        self.console.print(Rule(self.func_name()))
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
    
    @clock
    def Pi_Innaccurate(self, terms = 1000000):
        '''Calculate Pi using the Nalinkantha series'''
        self.console.print(Rule(self.func_name()))

        setcontext(Context(prec = terms))
        pi = Decimal(3)
        sign = 1
        number = 2
        
        while number < terms:
            pi += Decimal((sign * 4) / (number * (number + 1) * (number + 2)))
            sign *= -1
            number += 2

        return pi
    
    @clock
    def Eulers_Number(self, terms = 10000):
        '''Euler's number calculated as The infinite series 1 + 1/1! + 1/2! + 1/3! + ...
          can be used to calculate e. 
        Each term in the series represents a factorial 
        (the product of all positive integers up to that number). 
        For instance, 1! = 1, 2! = 2 * 1 = 2, 3! = 3 * 2 * 1 = 6, and so on. '''
        self.console.print(Rule(self.func_name()))

        euler = 2
        factorial = [1]
        for index in range(1, terms):
            factorial.append(factorial[index - 1] * (index + 1))
            euler += 1 / factorial[index]

        return euler
    
    @clock
    def Calculator(self):
        self.console.print(Rule(self.func_name()))
        x = int(input('What is x? '))
        y = int(input('What is y? '))

        return x + y
    
    @clock
    def square(self, number):
        self.console.print(Rule(self.func_name()))

        return number * number
    
    @clock
    def area_circle(self, radius):
        self.console.print(Rule(self.func_name()))
        return 2 * np.pi * radius ** 2
    
    @clock
    def Prime_Numbers(self, count):
        '''
        Return a list of some count of prime numbers
        
        >>> Problems.Prime_Numbers(10)
        [2, 3, 5, 7, 11, 13, 17, 19, 23]

        >>> Problems.Prime_Numbers(5)
        [2, 3, 5, 7]
        '''
        self.console.print(Rule(self.func_name()))

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

    @clock
    def Sieve_of_Erathostenes_Prime_Set(self, limit):
        self.console.print(Rule(self.func_name()))
        
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

    
    @clock
    def collatz_conjecture(self, limit):
        self.console.print(Rule(self.func_name()))

        collatz_sequences = []
        seed = 1
        # first you add the seed to the sequence, do the math, add each current to list until 1 or loop,
        # rich.print(collatz_sequences)        
        while seed <= limit:
            # if the current is an existing seed, then follow the existing seed trail
            subsequence = []
            subsequence.append(seed)
            current = seed
            while True:
                match current:
                    case current if current % 2 == 0:
                        current = int(current / 2)
                    case current if current % 2 != 0:
                        current = int(current * 3 + 1)
                if current in subsequence and current != 1:
                    rich.print(f'Loop found:\n{subsequence}')
                    break
                subsequence.append(current)
                if current == 1:
                    break
            collatz_sequences.append(subsequence)
            seed += 1
        for s in collatz_sequences:
            plt.plot(s) # x-axis defaults to 0, 1, 2, 3... for each line
        plt.show()
        return collatz_sequences
    
    @clock
    def odd_numbers(self, limit):
        # every odd number can be expressed as 2n + 1 starting from zero
        '''
        Critics of the stochastic approach argue that there could be a 
        specific "island" of numbers that always result in only a 
        single division by 2, causing the sequence to grow to infinity.
        '''
        # initialize variables
        number = 0
        odds = []
        div_2 = []
        while number < limit:
            # produce a list of odd numbers for examination
            odds.append(2 * number + 1)
            number += 1
        return odds
    @clock
    def even_numbers(self, limit):
        return
        # every even number can be expressed as k = 2n starting from 1

    @clock
    def three_N_plus_1(self, odds):
        '''
        The purpose of this method is to examine if there is any special
        properties of the proper subset of numbers that result from this set
        '''
        collatz_function1 = []
        for odd in odds:
            new = 3 * odd + 1
            collatz_function1.append(new)
        return collatz_function1
    @clock
    def find_repeating_decimal(self, numerator, denominator):
        # Get the integer part first (e.g., 1/7 -> 0)
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        if remainder == 0:
            return str(integer_part)  # No decimal part

        decimal_digits = []
        seen_remainders = {} # Remainder -> Index in decimal_digits

        while remainder != 0:
            # If we've seen this remainder before, we found the loop!
            if remainder in seen_remainders:
                loop_start = seen_remainders[remainder]
                non_repeat = "".join(decimal_digits[:loop_start])
                repeat = "".join(decimal_digits[loop_start:])
                return f"{integer_part}.{non_repeat}({repeat})"
            
            # Mark where this remainder first appeared
            seen_remainders[remainder] = len(decimal_digits)
            
            # Long division logic: multiply by 10 and divide
            remainder *= 10
            digit = remainder // denominator
            decimal_digits.append(str(digit))
            remainder %= denominator

        # If the loop finishes without finding a repeat (terminating decimal)
        return f"{integer_part}." + "".join(decimal_digits)