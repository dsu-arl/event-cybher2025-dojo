import sys
from time import sleep

def encipher(alphabet:list, NL:dict, plainText:str, indexPosition:int):
    cipherList = alphabet[indexPosition:] + alphabet[:indexPosition]
    cipherNumbers = {i:letter for i,letter in enumerate(cipherList)}

    cipherText = [cipherNumbers[NL[letter]] for letter in plainText]

    return "".join(cipherText)

def decipher(alphabet:list, LN:dict, cipherText:str, indexPosition:int):
    cipherList = alphabet[indexPosition:] + alphabet[:indexPosition]
    cipherLetters = {letter:i for i,letter in enumerate(cipherList)}

    plainText = [LN[cipherLetters[letter]] for letter in cipherText]

    return "".join(plainText)

if __name__ == "__main__":

    alphabet = list(("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-","*","?","#"))

    letterToNumber = {letter:i for i,letter in enumerate(alphabet)}
    numberToLetter = {i:letter for i,letter in enumerate(alphabet)}
    
    print('{:^71s}'.format("~*~*~EXAMPLE~*~*~"))
    print("|---------------------------------------------------------------------|")
    print("| ~*~What follows is an example of how the ciphertext was created.~*~ |")
    print("|    ~*~Follow the prompts to practice generating ciphertext.~*~      |")
    print("|---------------------------------------------------------------------|")
    print("\n\n")
    try:
        alphabetShift = int(input("How many characters should the alphabet shift: "))
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    
    textToEncode = str(input("Enter your text to encipher: "))

    for letter in textToEncode:
        try:
            letterToNumber[letter]
        except:
            print(f"ERROR: '{letter}' is not a valid character in this alphabet.")
            sys.exit(1)

    cipherText = encipher(alphabet,letterToNumber, textToEncode, alphabetShift)    
    plainText = decipher(alphabet,numberToLetter,cipherText,alphabetShift)

    print(f"Plaintext is:       {textToEncode}")
    print("_------------------------------")
    sleep(1)
    print(f"Enciphered text is: {cipherText}")
    sleep(1)
    print(f"Deciphered text is: {plainText}")
    sleep(1)
    print("\n\n")
    print('{:^71s}'.format("~*~*~CHALLENGE~*~*~"))
    print("|---------------------------------------------------------------------|")
    print("|{:^69s}|".format("The enciphered text is: 'kvndjhuhybdmypknldtbz-lybe'"))
    print("|{:^69s}|".format("Generate different alphabets to use to find the plaintext that"))
    print("|{:^69s}|".format("generates this ciphertext."))
    print("|---------------------------------------------------------------------|")

    try:
        alphabetShift = int(input("How many characters should the alphabet shift: "))
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    
    shiftedAlphabet = alphabet[alphabetShift:] + alphabet[:alphabetShift]
    print(f"Cipher alphabet is   : {shiftedAlphabet}")
    print(f"Plaintext alphabet is: {alphabet}")