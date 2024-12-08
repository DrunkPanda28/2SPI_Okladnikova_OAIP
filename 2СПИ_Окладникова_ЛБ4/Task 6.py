a = input(str())
vowels = ('аоуэыяёюеи')
count = 0
words = a.strip().split()
for word in words:
    for num in word:
        if num in vowels:
            count += 1
print(count)