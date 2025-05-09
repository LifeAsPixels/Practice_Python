from Practice import Problems
import time

def main():

    t0 = time.time()
    
    Instance = Problems.Problems()

    Instance.Fibonacci(8)
    print(Instance.Fizz_Buzz(15))
    print(Instance.isPalindromeNumber(150))
    # Instance.RockPaperScissors()
    
    
    print(Instance.Pi_Innaccurate())
    
    t1 = time.time()
    print(f'Program took {t1-t0:.4f} seconds to execute.')

if __name__ == "__main__":
    main()