# adieu, adieu


a={}
i=0

while True:
    try:
        user_input = input("Name: ")
        a[i] = user_input
        i+=1
        name_count = len(a)
        name_list = list(a.values())



    except EOFError:
        for i in range(name_count):
            # i names , i-1 commas
           print(name_list.pop())
           # print("\n Adieu, adieu, to",))

        break