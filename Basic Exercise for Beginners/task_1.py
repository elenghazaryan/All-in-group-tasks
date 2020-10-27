#Question1
def product_or_sum(num1, num2):
    product = num1 * num2
    summary = num1 + num2
    if product > 1000:
        return summary
    else:
        return product


#Question2
def sum_in_range():
    print("Printing current and previous number sum in a given range(10)")
    for i in range(10):
        if i == 0:
            print("Current Number {}, Previous Number {}, Sum: {}".format(0, 0, 0))
        else:
            print("Current Number {}, Previous Number {}, Sum: {}".format(i, i-1, 2 * i - 1))


#Question3
def even_index_printing(given_str):
    for i in range(0, len(given_str), 2):
            print(given_str[i])


#Question4
def remove_chars(given_str, n):
    if n < len(given_str):
        return given_str[n:]


#Question5
def same_first_last(given_list):
    if given_list[0] == given_list[-1]:
        return True
    else:
        return False


#Question6
def five_divisible(given_list):
    print("Given list is ", given_list)
    print("Divisible of 5 in a list")
    for i in given_list:
        if i % 5 == 0:
            print(i)


#Question7
def emma_count(given_str):
    print("Emma appeared {} times".format(given_str.count("Emma")))


#Question8
def pyramid():
    for i in range(6):
        print(i*'{} '.format(i))


#Question9
def is_reverse(given_num):
    my_num = given_num
    n = 0
    while given_num > 0:
        a = given_num % 10
        given_num = given_num // 10
        n *= 10
        n += a
    if n == my_num:
        return "The original and reverse number is the same"
    else:
        return "The original and reverse number is not same"
               

#Question10
def merging_lists(list1, list2):
    list3 = []
    for i in list1:
        if i % 2 != 0:
            list3.append(i)
    for i in list2:
        if i % 2 == 0:
            list3.append(i)
    print("First List:\t{}".format(list1))
    print("Second List:\t{}".format(list2))
    print("result List is:\t{}".format(list3))


#Question11
def extract_digits(number):
    while number > 0:
        digit = number % 10
        number //= 10
        print(digit, end=" ")


#Question12
def income_tax(given_income):
    pass


#Question13
def mul_table():
    for i in range(1,11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print("\n")


#Question14
def half_pyramid():
    for i in range(5, 0, -1):
        print(i*"* ")


#Question15
def exponent(given_num, given_exp):
    return given_num ** given_exp


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../15, 0 to QUIT\t"))
        if case == 1:
            number1 = int(input("Input first integer number:\t"))
            number2 = int(input("Input second integer number:\t"))
            print(product_or_sum(number1, number2))
        elif case == 2:
            sum_in_range()
        elif case == 3:
            inputed_string = input("Input your string line:\t")
            even_index_printing(inputed_string)
        elif case == 4:
            inputed_string = input("Input your string line:\t")
            remove_nums = int(input("Input the number of removing chars:\t"))
            print(remove_chars(inputed_string, remove_nums))
        elif case == 5:
            print(same_first_last([1, 0, 9, 8]))
        elif case == 6:
            print(five_divisible([1, 5, 6, 8, 10, 11, 55]))
        elif case == 7:
            sentence = "Emma is good developer. Emma is a writer. Emma is a singer"
            emma_count(sentence)
        elif case == 8:
            pyramid()
        elif case == 9:
            num = int(input("Input your number to check reverse:\t"))
            print(is_reverse(num))
        elif case == 10:
            merging_lists([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
        elif case == 11:
            num = int(input("Input the number to extract digits:\t"))
            extract_digits(num)
        elif case == 12:
            pass
        elif case == 13:
            mul_table()
        elif case == 14:
            half_pyramid()
        elif case == 15:
            num = int(input("Input your number:\t"))
            exp = int(input("Input the exponent:\t"))
            print(exponent(num, exp))
        elif case == 0:
            break
        else:
            print("Please enter the correct question number")