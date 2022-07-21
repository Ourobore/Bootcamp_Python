# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

print(f"{kata[1]}/{kata[2]}/{kata[0]} {kata[3]}:{kata[4]}")

# Other method with datetime library
import datetime
d = datetime.datetime(*kata)
print("{:%m/%d/%Y %H:%M}".format(d))
