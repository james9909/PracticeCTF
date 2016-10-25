cipher = open('encrypted.txt', 'r').read()
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decode(cipher):
    cipher = cipher.upper()
    for key in range(len(LETTERS)):
         translated = ''

         for symbol in cipher:
             if symbol in LETTERS:
                 num = LETTERS.find(symbol) # get the number of the symbol
                 num = num - key

                 if num < 0:
                     num = num + len(LETTERS)

                 translated = translated + LETTERS[num]

             else:
                 translated = translated + symbol

         print('Key #%s: %s' % (key, translated))

decode(cipher)
