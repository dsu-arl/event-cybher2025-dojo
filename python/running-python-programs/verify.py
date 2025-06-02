#!/usr/bin/exec-suid --real -- /usr/bin/python -I
import sys
sys.path.append('/challenge')

def print_flag():
    try:
        with open("/flag", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: Flag file not found.")

def main():
    print("You ran your first python program!")
    print("Here is your flag: ")
    print_flag()

if __name__ == "__main__":
    main()

# Add your imports and other code below here
