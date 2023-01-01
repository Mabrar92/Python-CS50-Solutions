
userinput = input("Input: ").strip()

a= ["a","A",]

for chr in userinput :
    if chr == "a" or chr == "i" or chr ==  "o" or chr == "u" or chr=="e":
        userinput = userinput.replace(chr,"")
    else :
        continue

print(userinput)