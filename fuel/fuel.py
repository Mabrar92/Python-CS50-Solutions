
def main():
    x = get_result()
    print(f"{x}%")


def get_result():

    while True:
        try:
            x = input("Fraction ")
            split_string = x.split("/")
            num =  int(split_string[0])
            denum = int(split_string[1])

            if num > denum :
                pass
            elif num <= denum :
                    return round(num/denum*100)

        except (ValueError,ZeroDivisionError) :
            pass

        else:
            break



main()
