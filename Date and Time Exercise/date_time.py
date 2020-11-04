import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time


#Question1
def print_current_time():
    print(datetime.datetime.now().time())


#Question2
def string_to_datetime():
    date_string = "Feb 25 2020  4:20PM"
    datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(datetime_object)


#Question3
def subtract_a_week():
    given_date = datetime(2020, 2, 25)
    print("Given date:   {}".format(given_date))
    days_to_substract = 7
    res_date = given_date - timedelta(days=days_to_substract)
    print("New date:  {}".format(res_date))


#Question4
def print_in_format():
    given_date = datetime(2020, 2, 25)
    print("Given date is")
    print(given_date.strftime('%A %d %B %Y'))


#Question5
def the_day_of_week():
    given_date = datetime(2020, 7, 26)
    print(given_date.today().weekday())
    print(given_date.strftime('%A'))


#Question6
def add_week_and_12hours():
    given_date = datetime(2020, 3, 22, 10, 00, 00)
    print("Given date")
    print(given_date)
    days_to_add = 7
    res_date = given_date + timedelta(days=days_to_add, hours=12)
    print("New Date")
    print(res_date)


#Question7
def current_time_in_milliseconds():
    milliseconds = int(round(time.time() * 1000))
    print(milliseconds)


#Question8
def convert_to_string():
    given_date = datetime(2020, 2, 25)
    string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
    print(string_date)


#Question9
def add_nmonths_from_current(months_to_add):
    given_date = datetime(2020, 2, 25).date()
    new_date = given_date + relativedelta(months=+ months_to_add)
    print(new_date)


#Question10
def difference_in_days():
    date_1 = datetime(2020, 2, 25).date()
    date_2 = datetime(2020, 9, 17).date()
    if date_1 > date_2:
        print("date_1 is greater")
        delta = date_1 - date_2
    else:
        print("date_2 is greater")
        delta = date_2 - date_1
    print("Difference is", delta.days, "days")


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            print_current_time()
        elif case == 2:
            string_to_datetime()
        elif case == 3:
            subtract_a_week()
        elif case == 4:
            print_in_format()
        elif case == 5:
            the_day_of_week()
        elif case == 6:
            add_week_and_12hours()
        elif case == 7:
            current_time_in_milliseconds()
        elif case == 8:
            convert_to_string()
        elif case == 9:
            n = int(input("How many months do you want to add?\t"))
            add_nmonths_from_current(n)
        elif case == 10:
            difference_in_days()
        elif case == 0:
            break
        else:
            print("Input correct question number")