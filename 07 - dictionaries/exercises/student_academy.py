students = {}

students_count = int(input())

for _ in range(students_count):
    name = input()
    grade = float(input())

    if name in students.keys():
        students[name].append(grade)
    else:
        students[name] = []
        students[name].append(grade)

for student, grades in students.items():
    if sum(grades) / len(grades) >= 4.50:
        print(f"{student} -> {sum(grades) / len(grades):.2f}")

