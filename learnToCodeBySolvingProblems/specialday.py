def is_special_day(month, day_of_month):
    if month == 2 and day_of_month == 18:
        return 'Special'
    elif month < 2 or (month == 2 and day_of_month < 18):
        return 'Before'
    else:
        return 'After'


if __name__ == '__main__':
    month = int(input())
    day_of_month = int(input())
    print(is_special_day(month, day_of_month))
