import random
import sys
import pyperclip

print(random.randint(1, 50))
print("Hello")
# sys.exit()
print("World")

pyperclip.copy("Hello World")
pyperclip.paste()