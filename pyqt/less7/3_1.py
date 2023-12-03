def calculate_time():
    try:
        with open("pipes.txt", "r") as file:
            lines = file.readlines()
        data = {}
        for i in lines[-1].split(" "):
            data[i] = lines[int(i) - 1].strip()
        total_time = 0
        for i in data:
            total_time += 100 / (60 * float(data[i]))
        with open("time.txt", "w") as output_file:
            output_file.write(str(float(100 / total_time)))

    except FileNotFoundError:
        pass
calculate_time()

