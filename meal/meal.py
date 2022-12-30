"""
breakfast---  7:00 and 8:00
lunch ---    12:00 and 13:00
dinner ---   18:00 and 19:00

"""

def main():

    time = input ("what time is it: ").lower().strip()
    time = time.split(":")
    hours = convert(time)

    if 7 <= hours <= 8 :
        print ("Breakfast Time")
    elif 12 <= hours <= 13 :
        print ("Lunch Time")
    elif 18 <= hours <= 19 :
        print ("Dinner Time")
    else :
        print()


def convert(time):
    time1 = float(time[0])
    time2 = float(time[-1])

    hours = round(time1 + time2/60,2)

    return hours



if __name__ == "__main__":
    main()