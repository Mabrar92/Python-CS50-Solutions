
"""
In the United States, dates are typically formatted in month-day-year order    (MM/DD/YYYY)

ISO 8601 year-month-day (YYYY-MM-DD)

Years with four digits,
months with two digits, a
nd days with two digits, “padding” each with leading zeroes as needed.



"""

Months = [
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
user_date = (input("Date: "))


is_numeric_date = False
##split the input into month-day-year
for chr in user_date.split():
    if chr == ("/"):
        is_numeric_date = True
        break

if is_numeric_date:
    data_mdy= user_date.split("/")


# if input has string go this way

    #split the input into month-day-year

    # compare month with the list if true : start conversion

    # convert into other date : store month day and year and print output with padding zeros in the form of (YYYY-MM-DD)

    # Extra checks ( day >! 31 ) ( Month >! 12 )

# if input has no string go this way



