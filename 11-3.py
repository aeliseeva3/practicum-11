sentence = input()
punctuation = ".,!?;:()\"'-«»/ ́`^...|"
words = [word.strip(punctuation) for word in sentence.split()]

print(words)

