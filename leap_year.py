#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program identifies leap years


def main():
    # This function indentifies leap years

    # input
    string = input("Enter a year: ")

    # process & output
    print("")
    try:
        year = int(string)
        if year % 4 != 0:
            print("{} is not a leap year.".format(year))
        elif year % 100 == 0 and year % 400 != 0:
            print("{} is not a leap year.".format(year))
        else:
            print("{} is a leap year.".format(year))
    except Exception:
        print("{} is not a year.".format(string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
