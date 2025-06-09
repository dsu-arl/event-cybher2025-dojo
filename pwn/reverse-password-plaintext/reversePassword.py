def selectorOne(sliceOne:list, sliceFour:list):
    
    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[sliceOneLen-2])
    partOne.append(sliceOne[sliceOneLen-4])
    partOne.append(sliceOne[sliceOneLen-8])
    partOne.append(sliceOne[sliceOneLen-5])
    
    return "".join(partOne)

def selectorTwo(sliceOne:list, sliceFour:list):

    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[3])
    partOne.append(sliceFour[sliceFourLen-7])
    partOne.append(sliceOne[5])
    partOne.append(sliceFour[sliceFourLen-1])
    
    return "".join(partOne)

def selectorThree(sliceOne:list, sliceFour:list):

    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[sliceOneLen-10])
    partOne.append(sliceFour[0])
    partOne.append(sliceOne[sliceOneLen-4])
    partOne.append(sliceFour[1])
    
    return "".join(partOne)

def main(stringOne:list, stringTwo:list):
    
    sliceOne = stringOne[0:10]
    sliceTwo = stringOne[10:20]
    sliceThree = stringOne[20:26]
    sliceFour = stringTwo[0:10]
    sliceFive = stringTwo[10:13]

    passwordPartOne = selectorOne(sliceOne, sliceFour)
    passwordPartTwo = selectorOne(sliceTwo, sliceFive)
    passwordPartThree = selectorTwo(sliceThree, sliceFour)
    passwordPartFour = selectorThree(sliceTwo, sliceFive)

    finalPassword = passwordPartTwo + passwordPartFour + passwordPartOne + passwordPartThree

if __name__ == "__main__":
    alphabet = list(("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"))
    special_char = list(("@","#","$","^","&","*","_","-","+","=","-","?"))
    main(alphabet, special_char)