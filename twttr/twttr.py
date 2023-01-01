
userinput = input("Input: ").strip()

a = ["a","A","e","E","i","I","o","O","u","U"]

for chr in userinput :
    for vowel in range(len(a)):
        if chr == vowel :
            userinput = userinput.replace(chr,"")
        else :
            continue

print(userinput)