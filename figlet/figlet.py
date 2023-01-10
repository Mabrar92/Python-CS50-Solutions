#Problem set 4 - Libraries - Problem no 2 - Solved by Muhammad Abrar


import sys
from pyfiglet import figlet





figlet = Figlet()

#for list of available fonts
figlet.getFonts()

#f is the font name as str
figlet.setFont(font=f)

# render the final output
print(figlet.renderText(s))