#Question1
def reverse_tuple():
    my_tuple = (10, 20, 30, 40, 50)
    my_tuple = my_tuple[::-1]
    print(my_tuple)


#Question2
def access_to_item():
    my_tuple = ("Purple", [10, 20, 30], (5, 15, 25))
    print(my_tuple[1][1])


#Question3
def create_with_single():
    single_item_tuple = (50, )
    print(single_item_tuple)


#Question4
def unpack():
    my_tuple = (10, 20, 30, 40)
    a, b, c, d = my_tuple
    print("a= {}, b= {}, c= {}, d= {}".format(a, b, c, d))


#Question5
def swap_tuples():
    tup1 = (55, 77)
    tup2 = (66, 88)
    tup2, tup1 = tup1, tup2
    print(tup1)
    print(tup2)


#Question6
def copy_to_new():
    tuple1 = (11, 22, 33, 44, 55, 66)
    tuple2 = tuple1[3:-1]
    print(tuple2)


#Question7
def modify():
    my_tuple = (11, [22, 33], 44, 55)
    my_tuple[1][0] = 222
    print(my_tuple)


#Question8
def sort_tuple():
    tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
    tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
    print(tuple1)


#Question9
def count_number():
    my_tuple = (50, 10, 60, 70, 50)
    print(my_tuple.count(50))


#Question10
def check():
    my_tuple = (55, 55, 55, 55)
    return all(i == my_tuple[0] for i in my_tuple)

if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            reverse_tuple()
        elif case == 2:
            access_to_item()
        elif case == 3:
            create_with_single()
        elif case == 4:
            unpack()
        elif case == 5:
            swap_tuples()
        elif case == 6:
            copy_to_new()
        elif case == 7:
            modify()
        elif case == 8:
            sort_tuple()
        elif case == 9:
            count_number()
        elif case == 10:
            print(check())
        elif case == 0:
            break
        else:
            print("Input correct question number")