from Practice.Problems import Problems, clock
import rich

@clock
def main():
    Instance = Problems()

    # Instance.Fibonacci(8)
    # print(Instance.Fizz_Buzz(15))
    # print(Instance.isPalindromeNumber(150))
    # # Instance.RockPaperScissors()
    
    # print(Instance.Pi_Innaccurate())
    # print(Instance.Eulers_Number(10000))
    
    # # print(Instance.Calculator())
    # print(Instance.square(8))
    # print(Instance.area_circle(3))

    print(Instance.Prime_Numbers(50))
    # print(Instance.Sieve_of_Erathostenes_Prime_Set(100))

    # Instance.Collatz_Conjecture(1000)
    # rich.print(Instance.find_repeating_decimal(1,12))
    # rich.print(len(Instance.collatz_conjecture(1000)))
    # odds = Instance.odd_numbers(100)
    # collatz_function1 = Instance.three_N_plus_1(odds)
    # print(collatz_function1)
    

if __name__ == "__main__":
    main()