#Question1
def reverse_the_list():
    a_list = [100, 200, 300, 400, 500]
    a_list.reverse()
    print(a_list)


#Question2
def concat_two_lists():
    list1 = ["M", "na", "i", "El"]
    list2 = ["y", "me", "s", "en"]
    list3 = [i + j for i, j in zip(list1, list2)]
    print(list3)


#Question3
def return_square():
    a_list = [1, 2, 3, 4, 5, 6, 7]
    print([x ** 2 for x in a_list])


#Question4
def my_order():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    res_list = [x + y for x in list1 for y in list2]
    print(res_list)


#Question5
def simultaneously_iteration():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    for x, y in zip(list1, list2[::-1]):
        print(x, y)


#Question6
def remove_empty_strings():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    resList = list(filter(None, list1))
    print(resList)


#Question7
def adding_item():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            reverse_the_list()
        elif case == 2:
            concat_two_lists()
        elif case == 3:
            return_square()
        elif case == 4:
            my_order()
        elif case == 5:
            simultaneously_iteration()
        elif case == 6:
            remove_empty_strings()
        elif case == 7:
            adding_item()
        # elif case == 8:
        #
        # elif case == 9:
        #
        # elif case == 10:
        #
        elif case == 0:
            break
        else:
            print("Input correct question number")