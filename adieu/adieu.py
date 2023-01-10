# adieu, adieu


a=[]
i=0

while True:
    try:
        user_input = input("Name: ")
        a[i] = user_input
        i+=1

    except EOFError:
        print("\n Adieu, adieu, to",user_input)
        break