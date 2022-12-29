#CS50 problem 2

greeting = input("Greeting : ").lower().strip()

if greeting == "hello" or greeting == "hello, newman":
    print ("$0")
elif greeting[0] == "h":
    print ("$20")
else :
    print ("$100")