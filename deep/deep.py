#CS50 first Question

word = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower().strip()

match word:
    case "forty two" | "forty-two" | "42" | "fortytwo":
        print ("Yes")
    case _:
        print ("No")
