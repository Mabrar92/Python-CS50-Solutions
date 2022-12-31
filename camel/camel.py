# A program that converts Camel Case names into Snake case

def main():

    name = input("camelCase:").strip()
    snakeconverter(name)





def snakeconverter(name):

    for capital in name:
        if capital.isupper():
            namepartition = name.partition(capital)
            
        else
            namepartition = name


    snake = namepartition[1]+ "_" + namepartition[2].lower()+ namepartition[3]

