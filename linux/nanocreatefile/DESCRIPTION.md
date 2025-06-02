## Nano Text Editor

In Linux, while you're using the command line, you'll probably need a way to edit files. 
On Windows we can use an app like notepad or Microsoft Word to edit files. 
Unfortunately, we don't have access to tools like this in the terminal because they are graphical tools. 
However, the Linux command line offers a wide range of text editors that we can use - one option is called `nano`.

You can use Nano by typing the command `nano {filename}` in the terminal.
If that filename already exists, it will open the existing file. 
Otherwise, it will create a new file with whatever filename you used. 
For example: `nano myfile.txt` will create a new text file named myfile.txt. 

You can then begin writing text to the screen as if you were using notepad on Windows. 
To move around in `nano` you will have to use the arrow keys. 
In `nano`, you can't use your mouse to click buttons like 'file' and 'save as' - you have to use Keyboard shortcuts. 
You're probably already familiar with certain keybaord shortcuts such as `CTRL+C` to copy, and `CTRL+V` to paste.

In nano, they provide you with all of the keyboard shortcuts you will need to use at the bottom of your screen. 
It shows you the shortcut you need to enter with the syntax of up carrot '^' and then a letter following it. 
The up carrot ('^') means you have to hold the control key and then hit the letter that follows to execute the proper function. 

To *save and close a file*, you will use the 'Exit' shortcut to save your file - `CTRL+X`. 
You will then be prompted if you want to "Save modified buffer", you can hit the 'y' key for yes to save your changes. 
Next it will ask you to confirm your filename at the bottom of the screen. 
It will be the filename you used when you ran nano, in our example "myfile.txt". 
To confirm your filename, press `Enter`. Or, if you'd like to change your filename, use the backspace button to delete it and then create a new name.

To put that all together for you, when you're done editing your file and are ready to save and close it: `CTRL+X` -> `y` -> `Enter`.

To complete this challenge you will use nano to create a file named `my_nano_file.txt` in your home directory (when you open the terminal, you will be in your home directory by default). This file should contain the phrase "CybHer 2025!". When you have put the text in your file, save and close it, then run `/challenge/solve` to verify that your file was made properly.

## Challenge Steps
1. Start the challenge and open a terminal
2. Use `nano` to create a file named `my_nano_file.txt`
3. Type the phrase "CybHer 2025!" in your file
4. Save and close your file: `CTRL+X` -> `y` -> `Enter`
5. Run `/challenge/solve` to verify your solution
6. Submit your flag
