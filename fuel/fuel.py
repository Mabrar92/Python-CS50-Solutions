
def main():
    x = get_result()
    print(x)

def get_result():

    try:
          x = int(input("Fraction"))
    except (ValueError,ZeroDivisionError) :
        pass
    else:
        split_string= x.split("/")
        num =  split_string[0]
        denum = split_string[1]
        return split_string


main()