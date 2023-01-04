

a={}
i = 0
while True:
    try :
        # Get the grocery list from the user
        user_input= input()
        # Store each item in the dict on the go
        a[i] = user_input
        i+=1

    except EOFError:

        #Sort Dict Values Alphabetically.
        list(a)
        #Output the values along with Count as prefix.

    except KeyError:
        pass