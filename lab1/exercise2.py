def find_min(list):

    """Return the minimum number from list.

    Arguments:
    list - input list which will be checked
    """

    min = list[0]
    for el in list:
        if int(el) < int(min):
            min = el

    return min

def find_max(list):

    """Return the maximum number from list.

    Arguments:
    list - input list which will be checked
    """

    max = list[0]
    for el in list:
        if int(el) > int(max):
            max = el

    return max

def calculate_centered_average(list):

    """Return the centered average of list.

    Arguments:
    list - input list which will be checked
    """

    list.remove(find_max(list))
    list.remove(find_min(list))

    sum = 0

    for el in list:
        sum = sum + int(el)

    return int(sum / len(list))
def main():
    numbers = input("Unesi brojeve razdvojene zarezima: ")
    print(calculate_centered_average(numbers.split(',')))

if __name__ == "__main__":
    main()