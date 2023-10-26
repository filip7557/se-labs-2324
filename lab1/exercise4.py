def check_string(string):

    """Count uppercase and lowercase letter and number and return a tuple of the three values.

    Arguments:
    string - input string which will be checked
    """
    lowercase = 0
    uppercase = 0
    numbers = 0

    uppercase_letters = "ABCČĆDDŽĐEFGHIJKLLJMNNJOPRSŠTUVZŽXQWY"
    lowercase_letters = str.lower(uppercase_letters)
    nums = "0123456789"

    for character in string:
        if character in nums:
            numbers = numbers + 1
        else:
            if character in uppercase_letters:
                uppercase = uppercase + 1
            elif character in lowercase_letters:
                lowercase = lowercase + 1

    return (uppercase, lowercase, numbers)

def main():
    string = input("Unesi string: ")
    print(check_string(string))

if __name__ == "__main__":
    main()