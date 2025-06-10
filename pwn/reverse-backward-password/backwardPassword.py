def selectorOne(sliceOne:list, sliceFour:list):
    
    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[sliceFourLen-1])
    partOne.append(sliceOne[sliceOneLen-2])
    partOne.append(sliceOne[sliceFourLen-2])
    partOne.append(sliceOne[sliceOneLen-7])
    
    return partOne

def selectorTwo(sliceOne:list, sliceFour:list):

    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[sliceOneLen-3])
    partOne.append(sliceFour[sliceFourLen-5])
    partOne.append(sliceOne[sliceOneLen-6])
    partOne.append(sliceFour[sliceFourLen-9])
    
    return partOne

def selectorThree(sliceOne:list, sliceFour:list):

    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[sliceOneLen-8])
    partOne.append(sliceFour[sliceFourLen-1])
    partOne.append(sliceOne[sliceOneLen-1])
    partOne.append(sliceFour[sliceFourLen-2])
    
    return partOne

def main(stringOne:list, stringTwo:list):
    
    # Contains 10 elements
    sliceOne = stringOne[3:13]

    # Contains 8 elements
    sliceTwo = stringOne[16:24]

    # Contains 8 elements
    sliceThree = list((stringOne[0],stringOne[1],stringOne[2],stringOne[13],stringOne[14],stringOne[15],stringOne[24],stringOne[25]))
    
    # Contains 10 elements
    sliceFour = stringTwo[0:10]
    
    # Contains 2 elements
    sliceFive = stringTwo[10:12]

    passwordPartOne = selectorOne(sliceOne, sliceFour)
    passwordPartTwo = selectorOne(sliceTwo, sliceFive)
    passwordPartThree = selectorTwo(sliceThree, sliceFour)
    passwordPartFour = selectorThree(sliceTwo, sliceFive)

    finalPassword = "".join(passwordPartFour + passwordPartTwo + passwordPartThree + passwordPartOne)

    finalPassword = finalPassword[::-1]
    

if __name__ == "__main__":
    alphabet = [a.upper() for a in list(("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"))]

    special_char = list(("@","#","$","^","&","*","_","-","+","=","-","?"))

    print("alphabet     = ", alphabet[::-1])
    print("special_char = ", special_char[::-1])

    main(alphabet[::-1], special_char[::-1])