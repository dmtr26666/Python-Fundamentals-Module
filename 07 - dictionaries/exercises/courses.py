courses = {}

while True:
    command = input()
    if ':' not in command:
        break

    course, name = command.split(' : ')

    if course in courses.keys():
        courses[course].append(name)
    else:
        courses[course] = []
        courses[course].append(name)

for course, students in courses.items():
    students_in_course = len(students)
    print(f"{course}: {students_in_course}")
    for student in students:
        print(f"-- {student}")