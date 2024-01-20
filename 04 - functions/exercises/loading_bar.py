def loading_bar(percent):
    bar = ['.'] * 10

    for i in range(percent // 10):
        bar[i] = '%'

    return bar

percent = int(input())
result = loading_bar(percent)
bar_string = ''.join(result)

if percent != 100:
    print(f"{percent}% [{bar_string}]")
    print("Still loading...")
else:
    print(f"{percent}% Complete!")
    print(f"[{bar_string}]")


