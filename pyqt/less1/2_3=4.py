classrooms = {}

day = input()
while day:
    while True:
        line = input()
        if not line:
            break

        subject, classroom = line.split()
        classroom = int(classroom)

        if classroom not in classrooms:
            classrooms[classroom] = set()

        classrooms[classroom].add(subject)

    day = input()
sorted_classrooms = sorted(classrooms.items())

for classroom, subjects in sorted_classrooms:
    subject_list = ", ".join(subjects)
    print(f"{classroom}: {subject_list}")
