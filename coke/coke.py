# A Coke Machine accepts only 5, 10, 25 cents. and in these input cases subtract from 50 until 0.

due = 50

while due > 0:
    coin = int(input("insert coin: "))

    if coin == 5 or coin == 10 or coin == 25 :
        due = due - coin
        if due > 0:
            print ("Amount Due:", due)
    else:
        print ("Amount Due:", due)

print ("Change owed:", -1*due)
