import sys

args = sys.argv
args.pop(0)

for arg in args:
    print("{}".format(str.swapcase(arg[::-1])), end="")
    if arg != args[-1]:
        print(" ", end="")
        
print()