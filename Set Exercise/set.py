#Question1
def add_to_set():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Green", "Blue", "Red"]
    sample_set.update(sample_list)
    print(sample_set)


#Question2
def identical_items():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    print(set1.intersection(set2))


#Question3
def marge_without_duplicates():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    print(set1.union(set2))


#Question4
def update_with_items():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    set1.difference_update(set2)
    print(set1)


#Question5
def remove_at_once():
    set1 = {10, 20, 30, 40, 50}
    set1.difference_update({10, 20, 30})
    print(set1)


#Question6
def sym_diff():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    print(set1.symmetric_difference(set2))


#Question7
def common_elements():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    if set1.isdisjoint(set2):
        print("Two sets have no items in common")
    else:
        print("Two sets have items in common")
        print(set1.intersection(set2))


#Question8
def update_set():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.symmetric_difference_update(set2)
    print(set1)


#Question9
def remove_not_common():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    print(set1)


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            add_to_set()
        elif case == 2:
            identical_items()
        elif case == 3:
            marge_without_duplicates()
        elif case == 4:
            update_with_items()
        elif case == 5:
            remove_at_once()
        elif case == 6:
            sym_diff()
        elif case == 7:
            common_elements()
        elif case == 8:
            update_set()
        elif case == 9:
            remove_not_common()
        elif case == 0:
            break
        else:
            print("Input correct question number")