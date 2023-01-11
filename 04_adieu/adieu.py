# adieu, adieu
import inflect

p=inflect.engine()
a={}
i=0

while True:
    try:
        user_input = input("Name: ")
        a[i] = user_input
        i+=1
        print(a)
        name_count = len(a)
        name_list = list(a.values())



    except EOFError:
        for name in a:
            print("\n Adieu, adieu, to",p.join(name_list[0:name+1]))
           # print()
            #for i in range(name_count):
                # i names , i-1 commas
            #print(mylist)

            #

        break