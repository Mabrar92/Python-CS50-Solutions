
userinput = input("Input: ").strip().lower()

for chr in userinput :
    if chr == "a" or chr == "i" or chr ==  "o" or chr == "u":
        userinput = userinput.replace(chr,"")
    else :
        continue

print(userinput)