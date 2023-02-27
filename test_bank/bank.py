#CS50 problem 2

def main():
    greeting = input("Greeting : ").lower().strip()
    print(value(greeting))

def value(greeting):

    if greeting == "hello" or greeting == "hello, newman":
        return 0

    elif greeting[0] == "h":
        return 20

    else :
        return 100

if __name__=="__main__":
    main()