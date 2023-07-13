'''
>>> JAAR
>>> 07/12/2023
>>> Practicing Fundamentals Program 4
>>> Version 1
'''

'''
>>> Generate a program that will take a year and will determine if the year inputted was a leap year or not.
'''


'''
>>> Takes the year inputted and test if it abides by the leap year rules.
    Param: year_entered : int
    Returns : bool
'''
def test_year(year_entered : int)->bool :
    if year_entered % 100 == 0 and year_entered % 400 != 0:
        return False
    if (year_entered % 4 != 0) :
        return False
    return True


def main() :
    response = 'yes'
    while response == 'yes' :
        year_entered = None
        while not isinstance(year_entered, int) or year_entered < 1582 :
            try :
                year_entered = int(input("Enter a year and I'll tell you if it's a leap year (based on Gregorian Calendar est 1582): " ))
                print(f'{year_entered = }')
                if year_entered < 1582 :
                    raise TypeError
            except ValueError :
                print('Your input was invalid')
            except TypeError :
                print(f"Your input was invalid. The Gregorian Calender was not in effect in the year{year_entered}.")

        leap_year = test_year(year_entered)
        if leap_year == True :
            print(f'{year_entered} is a leap year.')
        else :
            print(f"{year_entered} isn't a leap year.")
        # Assume the user response is either yes or no:
        response = input('Do you want to enter another year (yes/no): ').lower()

if __name__ == '__main__' :
    main()