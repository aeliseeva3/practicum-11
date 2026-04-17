lines = []
while True:
    s = input()
    if s == "":
        break
    lines.append(s)

text = " ".join(lines)

punctuation = ".,!?;:()\"'-"

for symbol in punctuation:
    text = text.replace(symbol, " ")

words = text.lower().split()

unique = []

for word in words:
    if word not in unique:
        unique.append(word)

counts = []

for word in unique:
    counts.append(words.count(word))

for first_word in range(len(unique)):
    for second_word in range(first_word + 1, len(unique)):
        if counts[first_word] < counts[second_word]:
            counts[first_word], counts[second_word] = counts[second_word], counts[first_word]
            unique[first_word], unique[second_word] = unique[second_word], unique[first_word]


for word in unique:
    print(word)

