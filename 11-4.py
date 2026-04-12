sentence = input()
punctuation = ".,!?;:()\"'-«»/ ́`^...|"
clean_words = [word.strip(punctuation) for word in sentence.split()]
unique_words = list(set(clean_words))

print(unique_words)

