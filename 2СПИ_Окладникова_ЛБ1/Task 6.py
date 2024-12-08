review = input("Введите отзыв: ")

words = review.split()
names = []

for word in words:
    if word.istitle():
        names.append(word)

result = '/'.join(names)

print("Назначить премию:", result)
