def count_letters(word):

counts = []
for i in range(len(word)):
    letter = word[i]
    matched = False 
    for j in range(len(counts)):
        if counts[j][0] == letters:
            counts[j][1] += 1
            matched = True 
            break
    if not matched:
        counts.append([letter, 1])
 return counts
 
 word = input("Enter a word: ")
 letter_counts = count_letters(word)
 
 for letterss, count in letter_counts:
    print(f"{letter}: {count}")
 
        
        
    