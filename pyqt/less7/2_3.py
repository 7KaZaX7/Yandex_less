def palindrome():
    try:
        with open("input.dat", 'rb') as file:
            data = file.read()
            rev_data = data[::-1]
            if data == rev_data:
                return True
            else:
                return False
    except FileNotFoundError:
        return False
