company_users = {}

while True:
    command = input()
    if '->' not in command:
        break

    company, ID = command.split(' -> ')

    if company in company_users.keys():
        if ID not in company_users[company]:
            company_users[company].append(ID)
    else:
        company_users[company] = []
        company_users[company].append(ID)

for company, students in company_users.items():
    students_in_course = len(students)
    print(f"{company}")
    for student in students:
        print(f"-- {student}")