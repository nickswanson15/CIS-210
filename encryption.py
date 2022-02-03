'''
Nick Swanson
basic encryption for a password - cybersecurity practice
18, April 2021
'''

def encrypt():
    '''encrypts by making each letter in the password go
    one letter further up in the alphabet; (i.e bat -> cbu)'''

    x = 0
    
    while x == 0:

        key = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f',
                'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
                'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
                'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
                'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z',
                'z': 'a', ' ': ' '
                }

        password = input("Please enter a password you would like to encrypt (stop to exit): ")
        password = password.lower()
        password = password.strip()
        encrypted = ''
        
        if password == 'stop':

            x = 1

        else:
            
            for letter in password:
                encrypted += key[letter]
            print(str(''))
            print(str('decrypted password: ' + password))
            print(str('encrypted password: ' + encrypted))

encrypt()
