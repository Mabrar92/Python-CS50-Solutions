# Vanity Plates

"""
1. All vanity plates must start with at least two letters
2. Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.

3. Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable
    vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.

4. No periods, spaces, or punctuation marks are allowed.
"""

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    check1 = False
    check2 = None
    letters_2 = s[0:2]
    letters_f = s[2:]
    numeric = 1

# Check for length 2 , any charachters 4 , first two charachters 1 .
    if 7 > len(s) > 1:
        if s.isascii():
            if letters_2.isalpha():
                check1 = True
                print("CHECK 1: TRUE")
    else:
             check1 = False

# Checking if Any Number comes in the middle

    for letter in letters_f:
        if letter.isalpha():
            
            continue
        elif letter.isnumeric():
            if numeric == 1 and letter == "0" :
                return False

            else:
                numeric+=1






"""
    if check1 and check2:
        return True
    else :
        return False
"""

main()