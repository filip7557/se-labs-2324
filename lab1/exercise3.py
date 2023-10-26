def calculate_centered_average(list):

    """Check if list contains two 2s next to eachother.

    Arguments:
    list - input list which will be checked
    """

    for i in range(len(list)):
        if list[i] == "2" and list[i+1] == "2":
            return True
        
    return False;

def main():
    numbers = input("Unesi brojeve razdvojene zarezima: ")
    print(calculate_centered_average(numbers.split(',')))

if __name__ == "__main__":
    main()