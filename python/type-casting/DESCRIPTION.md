## Challenge Description
***Input is only stored in strings, but how do we do math on strings?***
For example, how would we add 7 to the user's age? With the knowledge we've gained so far, we may try something like this:
```python
age = input("Enter your age: ")
future_age = age + 7
print("Age in the future", future_age)
```

Unfortunately, if you were to run the code above you would likely encouter a `TypeError`. 
This is because Python does not have the ability to do math on strings. 
So if you're expecting the user to input a numeric value, it will have to be converted from a group of _characters_ into a _number_, which can then be used throughout the rest of the program. 
Thankfully, Python allows "type casting" and makes this process very easy. 
In the example above, we can most likely assume that `age` is supposed to be an integer (a whole number) and the input we get from the user will need to be a number. 
To convert `age` from the input string to an integer/numberical value, you can "cast" it to an integer by using the `int()` function. 
The `int()` function takes a string variable, and gives you the integer value stored in that string.

For example:
```python
age = input("Enter your age: ") # read in as a string
age = int(age) # type cast to an int
future age = age + 3 # do some math
print("Age in the future", future_age) # print updated value
```

A shorter way to type the same thing is to call the `int()` function from *within* the `input()` function:
```python
# read in as a string, then immediately cast to an int
age = int(input("Enter your age: ")) 
future_age = age + 3
print("Age in the future", future_age)
```

Python will let you type cast to other data types as well. The functions you may need in the future are `int()`, `float()`, and `str()`. 

## Challenge Steps
Use python to calculate a users age + 7

1. Create a new file with the file extension `.py`
2. Write python to ask the user their age, and store that value as an integer
3. Calculate what their age will be in 7 years and print the resulting number (ONLY the number! No extra output)
4. Test your code with `python yourFile.py`
5. Verify your solution with `/challenge/verify yourFile.py`
```bash
# Example Running of the program
python yourScript.py
What is your age: 15
22
```
