
def main():
    x = get_result()
    print(x)


def get_result():

    while True:
        try:
            x = input("Fraction ")
            split_string = x.split("/")
            num =  int(split_string[0])
            denum = int(split_string[1])
        except (ValueError,ZeroDivisionError) :
            pass

        else:
            return split_string


main()
