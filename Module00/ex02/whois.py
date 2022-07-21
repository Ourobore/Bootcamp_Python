import sys

args = sys.argv
args.pop(0)

if len(args) == 0:
    print("Error: no argument is provided")
    exit()

if len(args) > 1:
    print("Error: more than one argument are provided")
    exit()

if not args[0].isnumeric():
    print("Error: argument is not a number")
    exit()

number = int(args[0])
if number == 0:
    print("I am Zero")
elif number % 2 == 0:
    print("I am Even")
else:
    print("I am Odd")

