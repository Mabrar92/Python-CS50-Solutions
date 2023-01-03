
def main():
    x = get_result()
    print(x)
def get_result(x):

    try:
          x = int(input("Fraction"))
    except (ValueError,ZeroDivisionError) :
        pass
    else:
        split_string= x.split("/")
        num =  split_string[0]
        denum = split_string[1]

        