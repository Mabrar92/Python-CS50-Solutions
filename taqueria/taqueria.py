
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

    b,c = get_item(food_items)
    print(f"\nTotal: ${b:.2f}")



def get_item(food_items):
    c = false
    a=0.00
    while True:
        try:
            user_items = input("Item: ").title()
            a+= food_items.get(user_items)

        except EOFError:
               print(c= !)
                return a,c

        except KeyError:
            pass


main()