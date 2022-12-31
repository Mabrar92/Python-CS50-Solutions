# A program that converts Camel Case names into Snake case

def main():

    name = input("camelCase:").strip()
    snake_name = snakeconverter(name)
    print ("snake_case:",snake_name)




def snakeconverter(name):

    for capital in name:
        if capital.isupper():
            namepartition = name.partition(capital)
            flag = True
            break
        else:
            namepartition = name
            flag = False

    if flag:
        snake = namepartition[0] + "_" + namepartition[1].lower() + namepartition[2]
        return snake
    else:
        return name

main()