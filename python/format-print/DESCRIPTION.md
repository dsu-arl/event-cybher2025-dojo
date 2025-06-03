## Challenge Description
Sometimes when we print variables, we want to include additional information to go with the value stored in a variable. 
This can be accomplished in a couple different ways. 

#### Print multiple values
The first way is simply combining multiple strings and variables together. 
You might remember that the value stored in a variable can be printed with the variable name (`print(var_name)`).
We can also print a string of hardcoded words (`print("This is a string")`) - the string must be wrapped in quotation marks. 
We can combine these two ways of printing information by putting them both in a single `print()` statement, with each part separated by commas.

Using the `name` variable we defined in the previous challenge, we could print a message before we print the value of `name` by doing something like this:
```python
print("Name is defined as", name) #Note the comma between the string and the variable!
```
When run, the program will output the following:
```commandline
Name is defined as The Rizzler
```
This is rather straightforward, but can become messy quickly if printing multiple variables and messages. 

#### Format strings
The other way we could print additional information is by using a **format string**. This requires some different pieces: 
- quotation marks to contain the entire string `""`
- the variable placeholders `{}` (these go in the quotes)
- the `.format()` function call (this goes after the quotes)
- the variables to be printed (these go in the `()` of the `.format()`)

Each placeholder `{}` is where a value will be printed. The order of your variables matters here - the first variable will print where the first placeholder is in your string.

If we put it all together, we can create some interactive prints. Using variables we defined previously, let's build out a format string:
```python
print("Hello {}, Your Total is: {}".format(name, total))
```
When running this code, we will get the following output:
```commandline
Hello The Rizzler, Your Total is: 1024.67
```


## Challenge Steps
Use python to create and print a variable with `.format`

1. Create a new file with the file extension `.py`
2. Create a python variable that contains a name
3. Write the python code to print the text `Hello, <name>` (where `<name>` is the name stored in your variable)
4. Test your code with `python yourFile.py`
5. Verify your solution with `/challenge/verify yourFile.py`
```bash
# Example program output
Hello, Rizzler
```
