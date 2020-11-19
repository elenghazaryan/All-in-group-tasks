#Question1
def convert_to_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    return_dict = dict(zip(keys, values))
    print(return_dict)


#Question2
def marge_dicts():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    print(dict1)


#Question3
def access_the_value():
    sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print(sample_dict["class"]["student"]["marks"]["history"])


#Question4
def with_default_values():
    employees = ['Kelly', 'Emma', 'John']
    defaults = {"designation": 'Application Developer', "salary": 8000}
    res_dict = dict.fromkeys(employees, defaults)
    print(res_dict)
    print(res_dict["Kelly"])


#Question5
def extract():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}
    keys = ["name", "salary"]
    new_dict = {k: sample_dict[k] for k in keys}
    print(new_dict)


#Question6
def keys_to_remove():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    keys_to_remove = ["name", "salary"]
    sample_dict = {k: sample_dict[k] for k in sample_dict.keys() -  keys_to_remove}
    print(sample_dict)


#Question7
def check_value(n):
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    print(n in sample_dict.values())


#Question8
def rename_key():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    sample_dict['location'] = sample_dict.pop('city')
    print(sample_dict)


#Question9
def key_of_min():
    sample_dict = {
          'Physics': 82,
          'Math': 65,
          'history': 75,
          'science': 34
        }
    print(min(sample_dict, key=sample_dict.get))


#Question10
def change_value():
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 6500}
    }
    sample_dict['emp3']['salary'] = 8500
    print(sample_dict)


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            convert_to_dict()
        elif case == 2:
            marge_dicts()
        elif case == 3:
            access_the_value()
        elif case == 4:
            with_default_values()
        elif case == 5:
            extract()
        elif case == 6:
            keys_to_remove()
        elif case == 7:
            num = int(input("Input your number to check:\t"))
            check_value(num)
        elif case == 8:
            rename_key()
        elif case == 9:
            key_of_min()
        elif case == 10:
            change_value()
        elif case == 0:
            break
        else:
            print("Input correct question number")