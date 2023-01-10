#Problem set 4 - Libraries - Problem no 2 - Solved by Muhammad Abrar


import sys
from pyfiglet import Figlet
import random




figlet = Figlet()
user_input = input("input:")

if len(sys.argv) < 2 :

    ran = random.randint(0,len(figlet.getFonts()))
    figlet.setFont(font=f)
    print(ran)



#for list of available fonts

print(len(figlet.getFonts()))

#f is the font name as str
#figlet.setFont(font=f)

# render the final output
#print(figlet.renderText(s))
