#Problem set 4 - Libraries - Problem no 2 - Solved by Muhammad Abrar


import sys
from pyfiglet import figlet

user_input = input("input:")

if len(sys.argv) > 1 :
    figlet.setFont(font=f)


figlet = Figlet()

#for list of available fonts
figlet.getFonts()

#f is the font name as str
figlet.setFont(font=f)

# render the final output
print(figlet.renderText(s))