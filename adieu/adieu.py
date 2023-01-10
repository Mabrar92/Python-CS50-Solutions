# adieu, adieu


a={}
i=0

while True:
    try:
        user_input = input("Name: ")
        a[i] = user_input
        i+=1
        name_count = len(a)


    except EOFError:
        for _ in range(name_count):
            #print("\n Adieu, adieu, to",list(a.values()))
            print(_)
        break