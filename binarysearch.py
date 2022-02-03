'''
Binary search

CIS 210 Winter 2021 Project 0-1

Author: Nick Swanson

Credits: N/A
'''

def ismemberI(aseq, target):
    '''(str) -> bool

    checks to see if a target in in a sequence and return True if it is and False if it is not
    
    >>> ismemberI((4, 5, 6), 4)
    True
    '''
    if target in aseq:
        return True
    if target not in aseq:
        return False

def ismemberR(aseq, target):
    '''(str) -> bool

    uses recursion to see if a target is in a sequence and returns true if it is and false if it is not
    
    >>> ismemberR((4, 5, 6), 5)
    True
    '''
    
    go = True
    while go == True:
        for i in range(len(aseq)):
            if aseq[i] == target:
                return True
                go = False
            else:
                return False

def bintest(f):
    '''(str) -> str

    calls both of the binary functions and return whether the test is true or false
    
    >>> bintest(ismemberI)
    checking ismemberI... True
    checking ismemberI... False
    '''
    if f == 'ismemberI':
        print('checking ismemberI...' + str(ismemberI((1, 2, 3, 3, 4), 3)))
        print('checking ismemberI...' + str(ismemberI((1, 2, 3, 3, 4), 99)))
        print('checking ismemberI...' + str(ismemberI('aeiou', 'i')))
        print('checking ismemberI...' + str(ismemberI('aeiou', 'y')))
        print('checking ismemberI...' + str(ismemberI((1, 3, 5, 7), 4)))
        print('checking ismemberI...' + str(ismemberI((23, 24, 25, 26, 27), 5)))
        print('checking ismemberI...' + str(ismemberI((0, 1, 4, 5, 6, 8), 4)))
        print('checking ismemberI...' + str(ismemberI((0, 1, 2, 3, 4, 5, 5), 3)))
        print('checking ismemberI...' + str(ismemberI((1, 3), 1)))
        print('checking ismemberI...' + str(ismemberI((2, 10), 10)))
        print('checking ismemberI...' + str(ismemberI((99, 100), 101)))
        print('checking ismemberI...' + str(ismemberI((42,), 42)))
        print('checking ismemberI...' + str(ismemberI((43,), 44)))
        print('checking ismemberI...' + str(ismemberI((' ',' '), 99)))
    if f == 'ismemberR':
        print('checking ismemberR...' + str(ismemberR((1, 2, 3, 3, 4), 3)))
        print('checking ismemberR...' + str(ismemberR((1, 2, 3, 3, 4), 99)))
        print('checking ismemberR...' + str(ismemberR('aeiou', 'i')))
        print('checking ismemberR...' + str(ismemberR('aeiou', 'y')))
        print('checking ismemberR...' + str(ismemberR((1, 3, 5, 7), 4)))
        print('checking ismemberR...' + str(ismemberR((23, 24, 25, 26, 27), 5)))
        print('checking ismemberR...' + str(ismemberR((0, 1, 4, 5, 6, 8), 4)))
        print('checking ismemberR...' + str(ismemberR((0, 1, 2, 3, 4, 5, 5), 3)))
        print('checking ismemberR...' + str(ismemberR((1, 3), 1)))
        print('checking ismemberR...' + str(ismemberR((2, 10), 10)))
        print('checking ismemberR...' + str(ismemberR((99, 100), 101)))
        print('checking ismemberR...' + str(ismemberR((42,), 42)))
        print('checking ismemberR...' + str(ismemberR((43,), 44)))
        print('checking ismemberR...' + str(ismemberR((' ',' ' ), 99)))

def main():
    '''(none) -> none

    calls the binary functions
    
    >>> main()
    '''
    bintest('ismemberI')
    bintest('ismemberR')

main()
