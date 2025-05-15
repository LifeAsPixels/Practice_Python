from Practice import Problems
import time

def main():

    
    Instance = Problems.Problems()

    Instance.Fibonacci(8)
    print(Instance.Fizz_Buzz(15))
    print(Instance.isPalindromeNumber(150))
    # Instance.RockPaperScissors()
    
    print(Instance.Pi_Innaccurate())
    print(Instance.Eulers_Number(10000))
    
    # print(Instance.Calculator())
    print(Instance.square(8))
    print(Instance.area_circle(3))

    print(Instance.Prime_Numbers(2000))
    # Instance.practice()
    t0 = time.time()
    print(Instance.Sieve_of_Erathostenes_Prime_Set(10000))
    t1 = time.time()

    print(f'Program took {t1-t0:.4f} seconds to execute.')

if __name__ == "__main__":
    main()