
food_items ={

    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00

}
a=0
while True:
    try:
        user_items = input("Item: ").title()
        if user_items in food_items :
            a+= round(food_items[user_items])

    except EOFError:
        print("\n")
        print(f"Total: ${a:.2f}")
        break
    except KeyError:
        pass



