import numpy


def question1():
    my_array = numpy.empty([4, 2], dtype=numpy.uint16)
    print("Created Array: \n", my_array)
    print("--Array Attributes--")
    print("Array Shape: {}\nArray dimensions: {}\nLength of each element in bytes: {}"
          .format(my_array.shape, my_array.ndim, my_array.itemsize))


def question2():
    my_array = numpy.arange(100, 200, 10)
    my_array = my_array.reshape(5, 2)
    print(my_array)


def question3():
    my_array = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
    new_array = my_array[..., 2]
    print(new_array)


def question4():
    my_arr = numpy.array([[3, 6, 9, 12], [15, 18, 21, 24],
                          [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
    new_arr = my_arr[1::2, ::2]
    print(new_arr)


def question5():
    array_one = numpy.array([[5, 6, 9], [21, 18, 27]])
    array_two = numpy.array([[15, 33, 24], [4, 7, 1]])
    res_of_arrays = array_one + array_two
    print("Addition of two arrays: ", res_of_arrays)

    for num in numpy.nditer(res_of_arrays, op_flags=['readwrite']):
        num[...] = num * num
    print(res_of_arrays)


def question6():
    my_arr = numpy.arange(10, 34, 1)
    my_arr = my_arr.reshape(8, 3)
    print(my_arr)
    sub_arrays = numpy.split(my_arr, 4)
    print(sub_arrays)


def question7():
    starting_arr = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    print("--Original Array--")
    print(starting_arr)

    sort_array_by_row = starting_arr[:, starting_arr[1, :].argsort()]
    print("--Sorting by second row--")
    print(sort_array_by_row)

    sort_array_by_column = starting_arr[starting_arr[:, 1].argsort()]
    print("-- Sorting by second column--")
    print(sort_array_by_column)


def question8():
    print("Printing Original array")
    sample_array = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    print(sample_array)

    min_of_axis_one = numpy.amin(sample_array, 1)
    print("Printing amin Of Axis 1")
    print(min_of_axis_one)

    max_of_axis_one = numpy.amax(sample_array, 0)
    print("Printing amax Of Axis 0")
    print(max_of_axis_one)


def question9():
    print("Printing Original array")
    sample_array = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    print(sample_array)

    print("Array after deleting column 2 on axis 1")
    sample_array = numpy.delete(sample_array, 1, axis=1)
    print(sample_array)

    arr = numpy.array([[10, 10, 10]])

    print("Array after inserting column 2 on axis 1")
    sample_array = numpy.insert(sample_array, 1, arr, axis=1)
    print(sample_array)



