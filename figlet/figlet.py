#Problem set 4 - Libraries - Problem no 2 - Solved by Muhammad Abrar


import sys
from pyfiglet import Figlet
import random




figlet = Figlet()

fonts= figlet.getFonts()


if len(sys.argv) == 1 :
    user_input = input("input:")
    ran = random.randint(0,len(fonts))
    figlet.setFont(font=fonts[ran])
    print(figlet.renderText(user_input))

elif len(sys.argv) > 2 and (sys.argv[1] == "-f" or sys.argv[2] == "-font") :
    user_input = input("input:")
    if sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))
    else :
        sys.exit("Invalid Usage")

else :
    sys.exit("Inavlid Usage")

