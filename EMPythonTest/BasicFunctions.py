# Task 1
def average(a, b):
    return (a + b) / 2


# Task 2
def reverse_list(input_list):
    return [ele for ele in reversed(input_list)]


# Task 3
def sort_numbers_descending(number_list):
    return sorted(number_list, reverse=True)


# Task 4
def add_indices(string_list):
    return [str(string_list.index(i) + 1) + '. ' + str(i) for i in string_list]


# Task 5
def capitalize_last_letter_in_each_word(string):
    s = str()
    for word in string.split():
        s += word[:-1] + word[-1].upper() + ' '
    return s[:-1]


# Task 6
def element_wise_merge(list1, list2):
    """
    Function that performs element-wise merge of list elements, inserting blank space in between
    :param list1: list of string
    :param list2: list of strings of the same length as list1
    :return: new list of merged strings
    """
    result = []
    for (ele1, ele2) in zip(list1, list2):
        result.append(ele1 + ' ' + ele2)
    return result


# Task 7
def execute_safely(operator, a, b):
    """
    Function that executes operator on arguments (a, b) -- or returns -1
    :param operator: some real-valued function, taking on input two real arguments
    :param a: a real number
    :param b: a real number
    :return: operator evaluated on (a,b) -- or -1 if this operation would be illegal
    """
    try:
        _ = operator(a, b)
    except:
        _ = -1
    return _
