# A program that converts Camel Case names into Snake case

def main():

    name = input("camelCase:").strip()
    snakeconverter(name)





def snakeconverter(name):

    for capital in name:
        if capital.isupper():
            name1,name2,name3= name.partition(capital)
        else
            snake=name


    snake = name1+ "_" + name2.lower()+ name3
    print(snake)
