"""
breakfast---  7:00 and 8:00
lunch ---    12:00 and 13:00
dinner ---   18:00 and 19:00

"""

def main():

    time = input ("what time is it: ").lower().strip()
    time = time.split(":")
    hours,minutes = convert(time)


    if 7 <= hours <= 8 :
        print ("Breakfast Time")
    elif 12 <= hours <= 13 :
        print ("Lunch Time")
    elif 18 <= hours <= 19 :
        print ("Dinner Time")
    else :
        print()


def convert(time):
    hours = float(time[0])
    minutes = float(time[-1])
    print (hours,minutes)
    return hours,minutes


if __name__ == "__main__":
    main()