# A program that converts Camel Case names into Snake case

name = input("camelCase:").strip()


for capital in name:
    if capital.isupper():
        print(capital)
        name1,name2,name3= name.partition(capital)


snake= name1+"_"+name2.lower()+name3
print(snake)
