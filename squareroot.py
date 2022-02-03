'''
Python variation.
CIS  210 Project 2-2 square root

Author: Nick Swanson

Credits: N/A

Comapring sqaure roots of numbers.

'''

def mysqrt(n, k):
    '''docstring -
    -   Integer > float  #type contract

    -  uses the babylonian formula to return the square root of a given number, n, and iterates it k times. #Breif description   

    -   mysqrt(25, 5)    #examples of use
        >> 5.0000231 
        mysqrt(25, 10)
        >> 5
        mysqrt(100, 10)
        >> 10
        mysqrt(625, 5)
        >> 29.182872
        mysqrt(1000, 8)
        >> 101.20218365
        mysqrt(1000, 10)
        >> 100.00000025
        mysqrt(1000, 11)
        >> 100.00
    '''
    x = 1
    for i in range(1, k + 1):
        x = 0.5*(x + n/x)
    return x

def sqrt_compare(num, iterations):
    '''docstring -
    -   Integer > float  #type contract

    -   calls the function mysqrt and compares it to the actual square root of a given number, and returns the percentage error. #Breif description     

    -  sqrt_compare(1000, 8)    #examples of use
        >> my sqrt value is: 101.202183
           math lib sqrt value is 100.0
           this is a 1.2 percent error.
    '''
    import math
    a = mysqrt(num, iterations)
    b = math.sqrt(num)
    c = abs(((b - a) / b) * 100)
    print("my sqrt value is " + str(a))
    print("math lib sqrt value is " + str(b))
    print(str(c) + ' percentage error')
    return None
    
def main():
    '''Sqaure root comaprison'''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()
