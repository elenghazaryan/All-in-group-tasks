#Question1
def name(name, age):
    print("{} is {} years old".format(name, age))


#Question2
def func1(*args):
    for i in args:
        print(i, end=" ")


#Question3
def calculation(num1, num2):
    print("Addition:\t{}, Subtraction:\t{}".format(num1+num2, num1-num2))


#Question4
def showEmployee(name, salary=9000):
    print("Employee {} salary is: {}".format(name, salary))


#Question5
def outer(a, b):
    def inner(a, b):
        return a + b
    result = inner(a, b)
    return result + 5


#Question6
def recursive_sum(num):
    if num:
        return num + recursive_sum(num - 1)
    else:
        return 0


#Question7
def display_student(name, age):
    print(name, age)


#Question8
def even_list():
    print(list(range(4, 30, 2)))


#Question9
def maximum(given_list):
    print(max(given_list))


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            n = input("Input your name:\t")
            a = int(input("Input your age:\t"))
            name(n, a)
        elif case == 2:
            func1(1, 2, 3, 4)
            print("")
            func1(1, 2)
        elif case == 3:
            n1 = int(input("Input number1:\t"))
            n2 = int(input("Input number12:\t"))
            calculation(n1, n2)
        elif case == 4:
            sal = int(input("Input your salary:\t"))
            nam = input("Input your name:\t")
            showEmployee(nam, sal)
            showEmployee(nam)
        elif case == 5:
            print(outer(5, 10))
        elif case == 6:
            print(recursive_sum(10))
        elif case == 7:
            show_student = display_student
            show_student("Elen", 20)
        elif case == 8:
            even_list()
        elif case == 9:
            maximum([1, 2, 6, 8, 3, 2, 6])
        elif case == 0:
            break
        else:
            print("Input correct question number")