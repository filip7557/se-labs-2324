def even_numbers_count(list):
    """Return the number of even numbers inside the list.

    Arguments:
    list - input list which will be checked
    """

    count = 0;

    for el in list:
        if int(el) % 2 == 0:
            count = count + 1
    
    return count

def main():
    numbers = input("Unesi brojeve razdvojene zarezima: ")
    print(even_numbers_count(numbers.split(',')))

if __name__ == "__main__":
    main()