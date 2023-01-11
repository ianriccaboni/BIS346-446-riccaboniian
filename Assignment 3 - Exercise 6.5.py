text = ('The Phillies are the 2022 National League Champions ' 
        'The Philadelphia Phillies defeated the San Diego Padres for the 2022 National League Championship')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    if count > 1:
        print(f'{word:<12}{count}')
