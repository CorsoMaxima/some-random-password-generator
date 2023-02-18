from datetime import datetime
import ctypes
from random import randrange
import string
import secrets
import winsound

themaxnumber = 30
final = ""

for _ in range(themaxnumber):
    yessir2 = randrange(1, 5)
    if yessir2 == 1:
        final += secrets.choice(string.ascii_lowercase)
    if yessir2 == 2:
        final += secrets.choice(string.ascii_uppercase)
    if yessir2 == 3 or yessir2 == 4:
        final += secrets.choice(string.digits)
    else:
        final += secrets.choice(string.punctuation)

with open('password.txt', 'w') as f:
    finalone = ""
    time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    password = final
    finalone = time + " / " + password
    f.write(finalone)
    winsound.MessageBeep(winsound.MB_OK)
    ctypes.windll.user32.MessageBoxW(0, "Your password.txt has been copied to the directory, where the script has ran.", "Password Generator v1", 0)