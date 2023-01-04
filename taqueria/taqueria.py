
def main():

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

    b = get_item(food_items)
    print(f"Total: ${b}")



def get_item(food_items):

    a=0.00
    while True:
        try:
            user_items = input("Item: ").title()
            a+= food_items.get(user_items)

        except EOFError:
                return a

        except KeyError:
            pass


main()