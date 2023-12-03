def reverse():
    with open('input.dat', 'rb') as file:
        data = file.read()
    with open('output.dat', 'wb') as file:
        file.write(data[::-1])


