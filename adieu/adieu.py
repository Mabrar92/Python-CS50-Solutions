# adieu, adieu




while True:
    try:
        user_input = input("Name: ")
        user_input+=user_input


    except EOFError:
        print("\n Adieu, adieu, to",user_input)
        break