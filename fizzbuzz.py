'''
FizzBuzz

CIS  210 Project 3-1 fizzbuzz

Author: Nick Swanson

Credits: N/A

counts up to an integer n, and prints fizz if the number is divisble by three, buzz if divisible by 5, and fizzbuzz if divisible by both.
'''

def fb(n):
    '''docstring
        -   Integer > None  #type contract

        -  counts up to an integer n, and prints fizz if the number is divisble by three, buzz if divisible by 5, and fizzbuzz if divisible by both.Dispplays game  over if integer, n, is reached and the number if not divisible by 3 or 5.
    '''
    
    for x in range(n):
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
            continue
        elif x % 3 == 0:
            print("fizz")
            continue
        elif x % 5 == 0:
            print("buzz")
            continue
        elif x % 3 != 0 or x % 5 != 0:
            print(x)
    print("Game Over!")
    
fb(15)
