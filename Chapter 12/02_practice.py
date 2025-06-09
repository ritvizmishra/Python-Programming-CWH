alphabets = ['apple', 'ball', 'cat', 'dog', 'egg', 'fish', 'goat', 'hen', 'ink', 'jug']

for i, items in enumerate(alphabets):
    if i >= 2 and i % 2 == 0 and i <= 7:
        print(f"{i+1}. {alphabets[i]}")
    else:
        continue