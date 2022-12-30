"""
breakfast---  7:00 and 8:00
lunch ---    12:00 and 13:00
dinner ---   18:00 and 19:00

"""

def main():

    time = input ("what time is it: ").lower().strip()
    time = time.split(":")
    convert(time)


def convert(time):
    time1 = float(time[0])
    time2 = float(time[-1])

    hours = time1 + time2/2

    print(hours)



if __name__ == "__main__":
    main()