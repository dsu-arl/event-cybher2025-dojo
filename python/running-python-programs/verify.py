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
    print("You ran your first python program!")
    print("Here is your flag: ")
    print_flag()

if __name__ == "__main__":
    main()

# Add your imports and other code below here
