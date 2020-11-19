#Question1
def merging_lists():
    list_one = [3, 6, 9, 12, 15, 18, 21]
    list_two = [4, 8, 12, 16, 20, 24, 28]
    list_three = []
    size1 = len(list_one)
    size2 = len(list_two)
    for i in range(1, size1, 2):
        list_three.append(list_one[i])
    for j in range(0, size2, 2):
        list_three.append(list_two[j])
    return list_three


#Question2
def removing_and_adding():
    sampleList = [34, 54, 67, 89, 11, 43, 94]
    print("Original list ", sampleList)
    element = sampleList.pop(4)
    print("List After removing element at index 4 ", sampleList)
    sampleList.insert(2, element)
    print("List after Adding element at index 2 ", sampleList)
    sampleList.append(element)
    print("List after Adding element at last ", sampleList)


#Question3
def slice_and_reverse(given_list):
    size = len(given_list)
    slice = size // 3
    if size < 6:
        print("Please input long list")
    else:
        list1 = given_list[:slice]
        list2 = given_list[slice:2*slice]
        list3 = given_list[2*slice:3*slice]
        print("Original list: {}".format(given_list))
        print("Chunk 1: {}".format(list1))
        print("After reversing it: {}".format(list(reversed(list1))))
        print("Chunk 2: {}".format(list2))
        print("After reversing it: {}".format(list(reversed(list2))))
        print("Chunk 3: {}".format(list3))
        print("After reversing it: {}".format(list(reversed(list3))))


#Question4
def create_dict(given_list):
    count_dict = dict()
    for i in given_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


#Question5
def list_pair_set():
    list1 = [2, 3, 4, 5, 6, 7, 8]
    list2 = [4, 9, 16, 25, 36, 49, 64]
    print("First List: ", list1)
    print("Second List: ", list2)
    print("Result: ", set(zip(list1, list2)))


#Question6
def find_intersection():
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    print("First Set ", first_set)
    print("Second Set ", second_set)

    intersection = first_set.intersection(second_set)
    print("Intersection is ", intersection)
    for item in intersection:
        first_set.remove(item)


#Question7
def check_subset():
    first_set = {57, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    print("First Set ", first_set)
    print("Second Set ", second_set)
    print("First set is subset of second set -", first_set.issubset(second_set))
    print("Second set is subset of First set - ", second_set.issubset(first_set))
    print("First set is Super set of second set - ", first_set.issuperset(second_set))
    print("Second set is Super set of First set - ", second_set.issuperset(first_set))
    if first_set.issubset(second_set):
        first_set.clear()
    if second_set.issubset(first_set):
        second_set.clear()
    print("First Set ", first_set)
    print("Second Set ", second_set)


#Question8
def list_dict():
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
    print("List -", roll_number)
    print("Dictionary - ", sample_dict)
    roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
    print("after removing unwanted elemnts from list ", roll_number)


#Question9
def dont_duplicate():
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
    print(set(list(speed.values())))


#Question10
def remove_and_create():
    sample_list = [87, 45, 41, 65, 94, 41, 99, 100]
    unique_items = list(set(sample_list))
    print("Unique items: ", unique_items)
    items_in_tuple = tuple(unique_items)
    print("min: ", min(items_in_tuple))
    print("max: ", max(items_in_tuple))


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            print(merging_lists())
        elif case == 2:
            removing_and_adding()
        elif case == 3:
            slice_and_reverse([11, 45, 8, 23, 14, 12, 78, 45, 89])
        elif case == 4:
            print(create_dict([11, 45, 8, 11, 23, 45, 23, 45, 89]))
        elif case == 5:
            list_pair_set()
        elif case == 6:
            find_intersection()
        elif case == 7:
            check_subset()
        elif case == 8:
            list_dict()
        elif case == 9:
            dont_duplicate()
        elif case == 10:
            remove_and_create()
        elif case == 0:
            break
        else:
            print("Input correct question number")