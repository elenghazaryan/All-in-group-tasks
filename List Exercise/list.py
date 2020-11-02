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


#Queston8
def list_extend():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sublist = ["h", "i", "j"]
    list1[2][1][2].extend(sublist)
    print(list1)


#Question9
def find_and_replace():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    index = list1.index(20)
    list1[index] = 200
    print(list1)


#Question10
def remove_value():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    for i in list1:
        if i == 20:
            list1.remove(i)
    return list1


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
        elif case == 8:
            list_extend()
        elif case == 9:
            find_and_replace()
        elif case == 10:
            print(remove_value())
        elif case == 0:
            break
        else:
            print("Input correct question number")