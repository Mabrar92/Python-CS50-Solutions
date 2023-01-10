#Problem set 4 - Libraries - Problem no 2 - Solved by Muhammad Abrar


import sys
from pyfiglet import Figlet
import random




figlet = Figlet()
user_input = input("input:")
fonts= figlet.getFonts()


if len(sys.argv) < 2 :
    ran = random.randint(0,len(fonts))
    figlet.setFont(font=fonts[ran])
    print(figlet.renderText(user_input))

elif len(sys.argv) > 2 :
    figlet.setFont(font=fonts[sys.argv[3]])
    print(figlet.renderText(user_input))





#for list of available fonts

print(len(figlet.getFonts()))

#f is the font name as str
#figlet.setFont(font=f)

# render the final output
print(figlet.renderText(s))
