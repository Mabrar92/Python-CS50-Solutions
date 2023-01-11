import emoji

while True:

    try:
        user_input = input("input: ")

        splitt = user_input.split(":")

        emojii = emoji.emojize(f":{splitt[1]}:")

        print(splitt[0], emojii, sep="")

        break

    except IndexError:
        pass
