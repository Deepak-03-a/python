def count_letters(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count
def count_all_letters(word):
    unique_letters = set(word)
    for letter in unique_letters:
        count = count_letters(word, letter)
        print(f"{letter}: {count}")
word = input("Enter a word: ")
count_all_letters(word)