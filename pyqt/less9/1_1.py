with open('input.bmp', 'rb') as file:
    baze = file.read(54)
    all = file.read()
negative = bytes([255 - i for i in all])
file.close
with open('res.bmp', 'wb') as out_file:
    out_file.write(baze)
    out_file.write(negative)