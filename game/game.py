import random

user_level = int(input("Level: "))
random.randint(0,user_level)
while True:
    try:
        if user_level < 0:
            continue
        else:
            user_guess= input("Guess: ")

            if user_guess > 0 :
                if user_guess > user_level:
                    print()
                elif user_guess < user_level:


                else:
                    print("just Right!")
                    break
        break
    except ValueError:
        pass