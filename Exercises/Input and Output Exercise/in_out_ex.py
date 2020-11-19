import os

#Question1
def mul(num1, num2):
    return num1 * num2


#Question2
def display_with_asterisk():
    print('My', 'name', 'is', 'James', sep="**")


#Question3
def decimal_to_octal(num):
    print('%o' % num)


#Question4
def floor(num):
    print('%.2f' % num)


#Question5
def input_numbers_to_list(list_size):
    my_list = []
    for i in range(list_size):
        my_list.append(float(input("Input list item[{}]:\t".format(i))))
    return my_list


#Question6
def removing_from_file():
    with open("Input and Output Exercise/file.txt", "r") as f:
        lines = f.readlines()
        print(lines)
        cnt = len(lines)
        print(cnt)
    with open("Input and Output Exercise/newfile.txt", "w") as f:
        for i in range(cnt):
            if i == 4:
                continue
            else:
                f.write(lines[i])


#Question7
def three_string():
    n, m, k = input("Input your 3 strings:\t").split()
    print(n, m,  k)


#Question8
def some_data():
    totalMoney = 1000
    quantity = 3
    price = 450.0
    print("I have {0} dollars so I can buy {1} football for {2:.2f} dollars".format(totalMoney, quantity, price))


#Question9
def file_is_empty():
    print(os.stat("Input and Output Exercise/file.txt").st_size == 0)


#Question10
def read_number_four():
    with open("Input and Output Exercise/file.txt", "r") as f:
        lines = f.readlines()
        cnt = len(lines)
    with open("Input and Output Exercise/newfile.txt", "w") as f:
        for i in range(cnt):
            if i == 3:
                f.write(lines[i])

if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            n1 = int(input("Input first number:\t"))
            n2 = int(input("Input second number:\t"))
            print(mul(n1, n2))
        elif case == 2:
            display_with_asterisk()
        elif case == 3:
            decimal_to_octal(57)
        elif case == 4:
            floor(576.878979)
        elif case == 5:
            size = int(input("Input list size:\t"))
            print(input_numbers_to_list(size))
        elif case == 6:
            removing_from_file()
        elif case == 7:
            three_string()
        elif case == 8:
            some_data()
        elif case == 9:
            file_is_empty()
        elif case == 10:
            read_number_four()
        elif case == 0:
            break
        else:
            print("Input correct question number")