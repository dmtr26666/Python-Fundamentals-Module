students = {}

while True:
    student_info = input()

    if ':' not in student_info:
        course_to_search = student_info
        break

    name, ID, course = student_info.split(':')

    students[name] = {}
    students[name][ID] = course


for k, v in students.items():
    for nested_key, nested_value in v.items():
        if nested_value.startswith(course_to_search[0:3]):
            print(f"{k} - {nested_key}")

