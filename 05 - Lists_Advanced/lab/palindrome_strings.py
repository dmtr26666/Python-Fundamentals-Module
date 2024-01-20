def find_palindrome(words):
    palindromes = []
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes

words_list = input().split()
palindrome = input()

palindromes_list = find_palindrome(words_list)
palindrome_counter = palindromes_list.count(palindrome)

print(palindromes_list)
print(f"Found palindrome {palindrome_counter} times")
