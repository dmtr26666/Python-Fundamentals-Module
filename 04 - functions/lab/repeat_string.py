string = input()
times_to_repeat = int(input())

repeat = lambda string, times: string * times

print(repeat(string, times_to_repeat))
