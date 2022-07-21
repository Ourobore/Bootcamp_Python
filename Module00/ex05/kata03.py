# Put this at the top of your kata03.py file
kata = "The right format"

# rjust / ljust method
print(kata.rjust(42, '-'), end="")

print()

# .format method
print(f"{kata:->42}", end="")