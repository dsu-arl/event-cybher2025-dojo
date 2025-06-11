## Challenge Description
There are a few other math operators commonly used in python:

- **Modulus:** `%` (e.g., `a % b`)
- **Exponent:** `**` (e.g., `a ** b`)
- **Floor Division:** `//` (e.g., `a // b`)

The exponent is fairly straight forward (how many times we are multiplying a number by itself). 
Modulus is like division, but returns the remainder. 
For example, `4%2` would return 0 since `2` can fit into `4` exactly twice (with a remainder of 0). 
What would `5%2` return? 

Floor division is just like division, but will round down if there is a remainder. 
For example, `5//2` would return `2`, whereas `5/2` would return `2.5`. 

We use these math operators the same way as the other ones: 
```python
# exponential (3^3 = 27) (3*3*3 = 27)
x = 3
y = 3

exp = x ** y

print("{} ^ {} = {}".format(x, y, sum))
```

The output will look like this:
```bash
# example output
3 ^ 3 = 27
```

## Challenge Steps
Use python to let the user enter a number and detect if that number is odd or even. Your program should print `0` for even and `1` for odd.

1. Create a new file with the file extension `.py`
2. Write the python code to get a number from the user (Don't forget to typecast)
3. Use modulus to show if the number is odd or even. Your program should print `0` for even and `1` for odd. *(Remember even numbers are always divisible by two)*
    (Hint: `5 % 2 = 1`, `8 % 2 = 0`)
4. Test your code with `python yourFile.py`
5. Verify your solution with `/challenge/verify yourFile.py` to get your flag
```bash
# example output
Please enter a number: 5
1
```

```bash
# example output
Please enter a number: 8
0
```
