string1 = input()
string2 = input()

last_string = string1

for i in range(len(string1)):
    current_string = string2[:i + 1] + string1[i + 1:]
    if current_string == last_string:
        continue
    else:
        last_string = current_string
        print(current_string)