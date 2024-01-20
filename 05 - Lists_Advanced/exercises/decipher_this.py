def decoder(word):
    number_as_list = [letter for letter in word if letter.isnumeric()]
    first_letter = chr(int(''.join(number_as_list)))

    coded_word = [letter for letter in word if not letter.isnumeric()]
    coded_word[0], coded_word[-1] = coded_word[-1], coded_word[0]
    decoded_word = ''.join(coded_word)

    return first_letter + decoded_word


coded_text = input().split()

decoded_text = []


for word in coded_text:
    decoded_text.append(decoder(word))

print(' '.join(decoded_text))