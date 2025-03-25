inches_snow = {'Monday': 2, 'Tuesday': 4, 'Wednesday': 5, 'Thursday': 1, 'Saturday': 0, 'Sunday': 0}



def total_snowfall(inches_snow):
    total_snow = 0
    for inches in inches_snow.values():
        total_snow += int(inches)
    print('Total snowfall inches:', total_snow)
total_snowfall(inches_snow)

inches_snow['Friday'] = input('how many inches fell on Friday? ')
total_snowfall(inches_snow)
