from ....py import Tutorial

class Problems:

    Util = cu()

    def Fibonacci(self, n):
        '''fibonacci sequence has two starting seeds 0 and 1 or 1 and 1
        each number is given a position like an index
        the most recent two numbers are added together to make the next number '''

        self.Util.Header()
        
        # instantiate the list with zeros at the size of the sequence n + 1
        fib = [0] * n
        fib[1] = 1
        for index in range(2, n):

            fib[index] = fib[index - 1] + fib[index - 2]
            # print(f'index: {index}  n: {n}')
        return fib
    