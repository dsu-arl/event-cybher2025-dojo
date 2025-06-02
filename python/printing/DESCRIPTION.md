## Challenge Description
Now it's time for you to write your own python program!
Just like if we were writing down the instructions to bake a cake, we need to create instructions for the computer to follow. 
These instructions will need to go in a python file with the `.py` file extension.
The computer will follow all of your instructions in order from top to bottom!
 
#### Python Printing
The first thing we are going to learn is how to print information to the screen, so you can see what your program is doing. In Python, to print to the screen, we will use the `print()` function (we will cover functions in more detail later).

When we use the `print()` function, the message that you want to print must be in quotes. Later, we will show you how to print other things too!
The `print()` function will always look something like this: 
```python
print("STRING MESSAGE TO PRINT")
```


For example, if we have a file named `test.py`, we can put the following contents in it:
```python
print("My Output!!")
```

We can run this file by using `python3`:
```commandline
python3 test.py
```

And then we will see this output displayed on the screen:
```commandline
My Output!!
```

#### Python Comments
In addition to printing things to the screen, you may sometimes need to add messages inside your code. This is called a comment. Comments can be useful to help explain Python code and make it more readable or to stop certain lines from executing. 

```python
# This is a comment
```

Comments start with a `#`, this is vital because it tells Python to ignore what follows. Comments can be placed on their own line, or at the end of an existing lines.

For example:
```python
# This is a greeting print statement
print("GREETINGS USER!") # Another Comment, do you think this is a good greeting?
```

You don't **need** to use comments, but we may include them in challenge descriptions, and they can be helpful for making notes in your programs :)

## Challenge Steps
Use python to print the text 'Hello World!' to the screen.

1. Use `nano` to create a new file, named whatever you want, but it must have the file extension `.py` (ex. `my_first_program.py`)
2. Use the `print()` function to print the text `Hello World!`
3. Test your code with `python3 yourFile.py`
4. Verify your solution with `/challenge/verify yourFile.py` to get your flag!
