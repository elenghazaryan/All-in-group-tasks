#Question1
def natural_numbers():
    for i in range(11):
        print(i)


#Question2
def pattern():
    for i in range(1, 6):
        for j in range(1, i+1):
            print(j, end=" ")
        print("")


#Question3
def sum_between_given_num(given_num):
    sum = 0
    for i in range(1, given_num+1):
        sum += i
    return sum


#Question4
def mul_of_num(given_num):
    for i in range(1, 11):
        print(given_num * i)


#Questin5
def list_members(given_list):
    for i in given_list:
        if i <= 150:
            if i % 5 == 0:
                print(i)
        else:
            break


#Question6
def digits_count(given_num):
    digits = str(given_num)
    print(len(digits))


#Question7
def reverse_pattern():
    for i in range(6, 0, -1):
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print("")


#Question8
def reverse_list(given_list):
    for i in range(len(given_list)-1, -1, -1):
        print(given_list[i])


#Question9
def display():
    for i in range(-10, 0, 1):
        print(i)


#Question10
def done():
    for i in range(5):
        print(i)
    else:
        print("Done!")


#Question11
def prime_in_range(start, end):
    for i in range(start, end):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


#Question12
def fibonacci():
    terms = 10
    num1, num2 = 0, 1
    count = 0

    print("Fibonacci sequence:")
    while count < terms:
        print(num1, end="  ")
        temp = num1 + num2
        num1 = num2
        num2 = temp
        count += 1


#Question13
def factorial(given_int):
    if given_int == 0 or given_int == 1:
        return 1
    else:
        return given_int * factorial(given_int - 1)


#Question14
def reverse_number(num):
    reverse_number = 0
    print("Given Number:\t", num)
    while num > 0:
        reminder = num % 10
        reverse_number = (reverse_number * 10) + reminder
        num = num // 10
    print("Reversed Number:\t", reverse_number)


#Question15
def even_position(my_list):
    for i in range(len(my_list)):
        if i % 2 != 0:
            print(my_list[i])


#Question16
def cube(given_num):
    for i in range(1, given_num+1):
        print("Current Number is : {} and the cube is {}".format(i, i ** 3))


#Question17
def sum_of_series(size):
    pass


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../15, 0 to QUIT\t"))
        if case == 1:
            natural_numbers()
        elif case == 2:
            pattern()
        elif case == 3:
            num = int(input("Input your number:\t"))
            print(sum_between_given_num(num))
        elif case == 4:
            num = int(input("Input your number:\t"))
            mul_of_num(num)
        elif case == 5:
            list_members([12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200])
        elif case == 6:
            num = int(input("Input your number:\t"))
            digits_count(num)
        elif case == 7:
            reverse_pattern()
        elif case == 8:
            reverse_list([10, 20, 30, 40, 50])
        elif case == 9:
            display()
        elif case == 10:
            done()
        elif case == 11:
            st = int(input("Input start of range:\t"))
            en = int(input("Input end of range:\t"))
            prime_in_range(st, en)
        elif case == 12:
            fibonacci()
        elif case == 13:
            num = int(input("Input your number:\t"))
            print("{}! = {}".format(num, factorial(num)))
        elif case == 14:
            number = int(input("Input number:\t"))
            print(reverse_number(number))
        elif case == 15:
            even_position([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        elif case == 16:
            number = int(input("Input your number:\t"))
            cube(number)
        elif case == 0:
            break
        else:
            print("Please enter the correct question number")