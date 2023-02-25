
def main():
    user_input= input("input: ").strip()
    print(shorten(user_input))



def shorten(word):
    a = ["a","A","e","E","i","I","o","O","u","U"]
    for chr in word:
        for vowel in a:
            if chr == vowel:
                word = word.replace(chr,"")
            else :
                continue

    return word

if __name__ == "__main__":
    main()