#!/usr/bin/exec-suid -- /usr/bin/python3.12 -I
import sys
sys.path.append('/challenge')

def print_flag():
    try:
        with open("/flag", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: Flag file not found.")

def main():
    password = input("Enter the password found in run_me.py: ")

    if password == "pythonrocks!":
        print("Password correct!")
        print("Here is your flag: ")
        print_flag()
    else:
        print("Wrong password!")

if __name__ == "__main__":
    main()

# Add your imports and other code below here
