# Vanity Plates

"""
1. All vanity plates must start with at least two letters
2. Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.

3. Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable
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

    letters = s[0:2]

    if 7 > len(s) > 1:
        if s.isascii():
            if letters.isalpha():
                s=True
    else:
        s = False

    for letter in s[3:-1] :
        if "0" in s :



main()