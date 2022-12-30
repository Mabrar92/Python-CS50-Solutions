"""
breakfast---  7:00 and 8:00
lunch ---    12:00 and 13:00
dinner ---   18:00 and 19:00

"""

def main():

    time = input ("what time is it: ").lower().strip()
    time = time.split(":")
    print(time)


def convert(time):
    time=time+1


if __name__ == "__main__":
    main()