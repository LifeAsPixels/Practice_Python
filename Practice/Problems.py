import inspect 

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

        for index in range(0, number + 1):
            match index:
                case index if (index % 3 == 0) and (index % 5 == 0):
                    print("fizzbuzz")
                case index if index % 3 == 0:
                    print("fizz")
                case index if index % 5 == 0:
                    print("buzz")
                case _:
                    print("...")


    def isPalindromeNumber(self, number: int):
        '''take in a max number
        iterate over every number through that number
        check if they are palindromes'''
        self.Util.Header()

        palindrome = []
        for item in range(0, number + 1):

            if str(item)[::-1] == str(item):
                palindrome.append(item)
        
        print(palindrome)
                