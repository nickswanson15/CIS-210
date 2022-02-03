'''
Paraity bits

CIS 210 Project 5-2 parity bits

Author: Nick Swanson

Credits: N/A

Encode a sequence of characters with parity bits, then check for parity bits and report any errors
'''

def encode(letter):

    '''docstring
        -   str > str  #type contract

        -  Adds a parity bit to the binary representation of letter.

        -   letter(c)         #examples of use
        >> 01100011

            letter(c)
        >> 11100100
    ''' 
    binary = bin(ord(letter))
    binary.replace('0b', '')

    x = parity(binary)

    new = x + binary

    return new

def parity(bitrep):

    '''docstring
        -   str > str  #type contract

        -  Determines the paraity bit for a binary sequence, given a string of 1s and 0s.

        -   parity(1100011)         #examples of use
        >> 0
            parity(1100100)
        >> 1
    '''

    total = sum(map(int, bitrep)

    if total % 2 == 0: 
        part = '0'
    else:
        part = '1'

    return part
    
def decode(pletter):

    '''docstring
        -   str > str  #type contract

        -  converts pletter, a string of binary plus parity bit, back into character and returns the character.

        -   decode(11001001)         #examples of use
        >> c
     '''
    if parity(pletter) == 0:
       return chr(int(pletter, 2))
    else:
        return('*')
                
def main():

    '''docstring
        -   None > str  #type contract

        -  encodes and decodes the characters in a word.

        -   main()         #examples of use
        >> 
    '''
    word = 'cat'
    for letter in word:
        print(decode(encode(letter)), end='')
        print()
        
if _name_ == '_main_':
    main()
