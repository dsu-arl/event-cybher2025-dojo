## Challenge Description
Lets put your skills to the test! There are many common formulas that mathematicians need to memorize! In geometry, for example...

**Finding the Area of shapes**  
Circle: `π*r²`  
Square: `s²`  
Triangle: `0.5 * b * h`  
Trapezoid: `((a + b) / 2) * h`  

To find the area of a square:
```python
s = float(input("Length of side: "))
area = s**2 # ** to find exponent

print("Area = ", area)
```

```bash
# example output
Length of side: 5
Area =  25.0
```

## Challenge Steps
Use python to read in the base and height (b and h) of a triangle using **floats**, then calculate and print the area.

Note: The area will be a float data type! Make sure to get user input and typecast it to a **float** (`float()` instead of `int()`).

1. Create a new file with the file extension `.py`
2. Write the python code to get two numbers from the user (triangle width and height)
3. Use the formula above to calculate the area of a triangle and print the result!
4. Test your code with `python yourFile.py`
5. Verify your solution with `/challenge/verify yourFile.py`
```bash
# example output
Base: 3
Height: 5
Area =  7.5
```
