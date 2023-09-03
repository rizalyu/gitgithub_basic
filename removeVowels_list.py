def remove_vowels(word):
    vowels = 'aeiouAEIOU'
    non_vowel_letters = [letter for letter in word if letter not in vowels]
    return non_vowel_letters

word = input()

result = remove_vowels(word)
print(result)