# A program that converts Camel Case names into Snake case

def main():

    name = input("camelCase:").strip()
    snake_name = snakeconverter(name)
    print ("snake_case:",snake_name)




def snakeconverter(name):

    for capital in name:
        if capital.isupper():
            snake =  name.replace(capital , "_" + capital.lower())
            flag = True
        else:
            continue

    if flag:
        return snake
    else:
        return name

main()