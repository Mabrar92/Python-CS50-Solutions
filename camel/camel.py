# A program that converts Camel Case names into Snake case

name = input("camelCase:").strip()


for capital in name:
    if capital.isupper():
        name=name.lower()
        print(capital)
        name= name.partition(capital)



print(name)
