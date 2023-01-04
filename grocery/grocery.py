

a={}
i = 0
while True:
    try :
        # Get the grocery list from the user
        user_input= input()
        # Store each item in the dict on the go
        a[i] = user_input
        print(a)
        i+=1

    except EOFError:

        #Get all the values and Sort Dict Values Alphabetically.
        grocery_list= list(a.values())
        grocery_list.sort()
        print(grocery_list)

        #Output the values along with Count as prefix.
        for item in grocery_list:
            print(item)
            #print(list.count(item),item)

        break

    except KeyError:
        pass