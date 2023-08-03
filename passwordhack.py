from string import ascii_letters, digits, punctuation
from itertools import product

#Cycle for genertaing all possible passwords
for passcode in product(ascii_letters + digits + punctuation, repeat=4):
  print(*passcode)
