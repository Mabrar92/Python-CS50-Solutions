import random

a=True
while True:
    try:
        if a:
            user_level = int(input("Level: "))
            level=random.randint(0,user_level)
            a=False
        if user_level < 0:
            a=True
            continue
        else:
            user_guess= int(input("Guess: "))

            if user_guess > 0 :
                if user_guess > level:
                    print("Too large!")
                    continue
                elif user_guess < level:
                    print("Too small!")
                    continue
                else:
                    print("Just right!")
                    break
        break
    except ValueError:
        a=True
        pass
