def sort_string(string):
    """
    The function converts a string into a sorted list.
    :param string: source string
    :return: result
    """
    chars = list(string)
    chars.sort()
    result = ''.join(chars)
    return result


input_string = input()
sorted_string = sort_string(input_string)

print(sorted_string)

