path = input().split("\\")

file_name = path[-1].split('.')

print(f"File name: {file_name[0]}")
print(f"File extension: {file_name[1]}")
