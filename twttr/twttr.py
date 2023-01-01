
userinput = input("Input").strip().lower()

for chr in userinput :
    if chr == "a" | "i" | "o" | "u" :
        userinput = userinput.replace(chr)
    else :
        continue:

