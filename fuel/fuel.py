
def main():
    x = get_result()

    if  100 >= x >= 99:
        print("F")
    elif  1 >= x >= 0:
        print("E")
    else:
        print(f"{x}%")


def get_result():

    while True:
        try:
            x = input("Fraction ")
            split_string = x.split("/")
            num =  int(split_string[0])
            denum = int(split_string[1])
            result = num/denum

            if result > 1 :
                    continue
            else:
                return round(num/denum*100)

        except (ValueError, ZeroDivisionError) :
            pass

main()

#