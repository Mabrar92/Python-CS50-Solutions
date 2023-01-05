
"""
In the United States, dates are typically formatted in month-day-year order    (MM/DD/YYYY)

ISO 8601 year-month-day (YYYY-MM-DD)

Years with four digits,
months with two digits, a
nd days with two digits, “padding” each with leading zeroes as needed.



"""

months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


#try:

#Take input from user
def main():

    while True:
        user_date = (input("Date: "))

        ##split the input into month-day-year
        if "/" in user_date:
            months,day,year = numeric_date(user_date)
        else:
             months,day,year = alpha_date(user_date)


        if day <= 31 and months <= 12 :
                print(f"{year}-{months:02}-{day:02}")
                break
        else:
            continue



def numeric_date(user_date):

        data_mdy = user_date.split("/")

        if data_mdy[0].isnumeric():
            months = int(data_mdy[0])
        else:
            months = 13

        day = int(data_mdy[1])
        year = int(data_mdy[2])

        return months,day,year


def alpha_date(user_date):

    try:
        data_mdy = user_date.split(",")

        if len(data_mdy) < 2:
            day = 32
            month = 13
            year = 1900
            return month,day,year
        else:
            year =int(data_mdy[1])
            data_md = data_mdy[0].split(" ")
            months = data_md[0]

        if data_md[1].isnumeric():
            day = int(data_md[1])

        else:
            day = 32
            month = 13
            return month,day,year

        #for months in range(len(months))
        month = months_list.index(months.title())+1

        return month,day,year

    except ValueError:
        pass

main()

# if input has string go this way

    #split the input into month-day-year

    # compare month with the list if true : start conversion

    # convert into other date : store month day and year and print output with padding zeros in the form of (YYYY-MM-DD)

    # Extra checks ( day >! 31 ) ( Month >! 12 )

# if input has no string go this way




