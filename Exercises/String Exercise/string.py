import re


#Question1
def get_middle_chars(given_str):
    size = len(given_str)
    sep = (size - 3)//2
    given_str = given_str[sep:size-sep]
    return given_str


#Question2
def append_in_the_middle(s1, s2):
    middle = len(s1) // 2
    print("{}{}{}".format(s1[:middle], s2, s1[middle:]))


#Question3
def strings(s1, s2):
    m1 = len(s1) // 2
    m2 = len(s2) // 2
    s3 = s1[0] + s2[0] + s1[m1] + s2[m2] + s1[-1] + s2[-1]
    return s3


#Question4
def lower_upper(given_str):
    lower = []
    upper = []
    for i in given_str:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    return_string = ''.join(lower + upper)
    print(return_string)


#Question5
def counting(given_str):
    digits = []
    lower = []
    upper = []
    special_symbols = []
    for char in given_str:
        if char.isdigit():
            digits.append(char)
        elif char.isupper():
            upper.append(char)
        elif char.islower():
            lower.append(char)
        else:
            special_symbols.append(char)
    print("Chars = {}\nUpper = {}\nLower = {}\nDigits = {}\nSymbols = {}"
          .format(len(lower + upper), len(upper), len(lower), len(digits), len(special_symbols)))


#Question6
def mixed_string(s1, s2):
    s2 = s2[::-1]
    lengthS1 = len(s1)
    lengthS2 = len(s2)
    length = lengthS1 if lengthS1 > lengthS2 else lengthS2
    resultString = ""
    for i in range(length):
        if (i < lengthS1):
            resultString = resultString + s1[i]
        if (i < lengthS2):
            resultString = resultString + s2[i]
    print(resultString)


#Question7
def string_balance_check(s1, s2):
    result = True
    for i in s1:
        if i in s2:
            continue
        else:
            result = False
    return result


#Question8
def finding(str, substr):
    count = str.lower().count(substr.lower())
    print("The {} count is {}:\t".format(substr, count))


#Question9
def digits():
    inputStr = "English = 78 Science = 83 Math = 68 History = 65"
    markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
    totalMarks = 0
    for mark in markList:
        totalMarks += mark

    percentage = totalMarks / len(markList)
    print("Total Marks is:", totalMarks, "Percentage is ", percentage)


#Question10
def count_chars(given_str):
    count_dict = dict()
    for i in given_str:
        count = given_str.count(i)
        count_dict[i] = count
    print(count_dict)


#Question11
def reverse_string(given_string):
    print(given_string[::-1])


#Question12
def pos_of_substr():
    str1 = "Emma is a data scientist who knows Python. Emma works at google."
    print("Original String is:", str1)
    index = str1.rfind("Emma")
    print("Last occurrence of Emma starts at", index)


#Question13
def split_to_substr():
    str1 = "Emma-is-a-data-scientist"
    print("Original String is:", str1)
    substrings = str1.split("-")
    print("Displaying each substring")
    for sub in substrings:
        print(sub)


#Question14
def removing_empty_strings():
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    print("Original list of sting")
    print(str_list)
    new_str_list = list(filter(None, str_list))
    print("After removing empty strings")
    print(new_str_list)


#Question15
def without_symbols():
    str1 = "/*Jon is @developer & musician"
    print("Original string is:\t ", str1)
    str2 = re.sub(r'[^\w\s]', '', str1)
    print("New string is:\t", str2)


#Question16
def only_digits():
    str1 = 'I am 25 years and 10 months old'
    print("Original string is", str1)
    res = "".join([item for item in str1 if item.isdigit()])
    print(res)


#Question17
def alphabets_numbers():
    pass


#Question18
def replacing():
    pass
    # str1 = '/*Jon is @developer & musician!!'
    # print("The original string is : ", str1)
    # replace_char = '#'
    # for char in punctuation:
    #     str1 = str1.replace(char, replace_char)
    # print("The strings after replacement : ", str1)


if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../15, 0 to QUIT\t"))
        if case == 1:
            print(get_middle_chars('JhonDipPeta'))
        elif case == 2:
            append_in_the_middle("Ault", "Kelly")
        elif case == 3:
            str1 = input("Enter s1:\t")
            str2 = input("Enter s2:\t")
            print(strings(str1, str2))
        elif case == 4:
            str = input("Enter your line:\t")
            lower_upper(str)
        elif case == 5:
            str = input("Enter your line:\t")
            counting(str)
        elif case == 6:
            str1 = input("Enter s1:\t")
            str2 = input("Enter s2:\t")
            mixed_string(str1, str2)
        elif case == 7:
            str1 = input("Enter s1:\t")
            str2 = input("Enter s2:\t")
            print(string_balance_check(str1, str2))
        elif case == 8:
            s = input("Input your line:\t")
            sub = input("Input what do you want to find:\t")
            finding(s, sub)
        elif case == 9:
            digits()
        elif case == 10:
            str = input("Enter your line:\t")
            count_chars(str)
        elif case == 11:
            str = input("Enter your line:\t")
            reverse_string(str)
        elif case == 12:
            pos_of_substr()
        elif case == 13:
            split_to_substr()
        elif case == 14:
            removing_empty_strings()
        elif case == 15:
            without_symbols()
        elif case == 16:
            only_digits()
        elif case == 17:
            alphabets_numbers()
        elif case == 18:
            replacing()
        elif case == 0:
            break
        else:
            print("Please enter the correct question number")