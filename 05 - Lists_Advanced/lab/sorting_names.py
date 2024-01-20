def sort_by_legth(names):
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return sorted_names

names = input().split(', ')
sorted_names = sort_by_legth(names)

print(sorted_names)
