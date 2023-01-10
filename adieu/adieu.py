# adieu, adieu


a={}
i=0

while True:
    try:
        user_input = input("Name: ")
        a[i] = user_input
        i+=1
        name_count = len(i)


    except EOFError:
        for _ in range(i):
            #print("\n Adieu, adieu, to",list(a.values()))
            print(_)
        break