## Challenge Description
Now that you know how to get input from a user and type cast it, you need to learn how to do things with that input. 
The first thing we are going to cover is math operators. 
Python supports many different **Math Operators**, we are going to start with just 4:

- **Addition:** `+` (e.g., `a + b`)
- **Subtraction:** `-` (e.g., `a - b`)
- **Multiplication:** `*` (e.g., `a * b`)
- **Division:** `/` (e.g., `a / b`)

You most likely already know how to add and subtract things, now you just need to learn how to write the python code to do it for you!
Here are some examples of doing math in python:
```python
a = 10
b = 5

add = a + b
sub = a - b
mul = a * b
div = a / b

print(add)
print(sub)
print(mul)
print(div)
```

Output:
```commandline
15
5
50
2
```

Here we are using separate variables to store all of the results, you can also re-use a variable if you'd like. Just be aware that once you update a value, the old one is gone forever!
This code:
```python
a = 10
b = 5

res = a + b
print(res)
res = a - b
print(res)
res = a * b
print(res)
res = a / b
print(res)
```
Will have the exact same output as above:
```commandline
15
5
50
2
```

## Challenge Steps
Add two numbers together!

1. Create a new file with the file extension `.py`
2. Get user input for 2 numbers (don't forget the prompts/type casting!)
3. Add those two numbers together
4. Print the result
5. Test your code with `python yourFile.py`
6. Verify your solution with `verify yourFile.py` to get the flag
```bash
# example output
Enter a number: 5
Enter another number: 7
12
```
