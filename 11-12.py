def count_holes(word):
    """
    Counts how many letters with holes are in a word.
    :param word: original word
    :return: count holles letters
    """
    holes_letters = set('abdegopq')
    count = 0
    for char in word:
        if char in holes_letters:
            count += 1
    return count


def count_letters(text):
    """
    Counts how many letters with and without holes are in the text.
    :param text: original text
    :return: count holles letter and no holles letter
    """
    holes_letters = set('abdegopq')
    holes = 0
    no_holes = 0
    
    for char in text:
        if char.isalpha():  
            if char in holes_letters:
                holes += 1
            else:
                no_holes += 1
    return holes, no_holes


def words_with_two_or_more_holes(text):
    """
    Words with 2 or more letters with holes.
    :param text: original text
    :return: words with 2 or more letters with holes
    """
    words = text.split()
    result = []
    for word in words:
        if count_holes(word) >= 2:
            result.append(word)
    return result


text = input().lower()

holes_count, no_holes_count = count_letters(text)

print(f"Буквы с отверстиями: {holes_count}")
print(f"Буквы без отверстий: {no_holes_count}")

filtered_words = words_with_two_or_more_holes(text)

print(filtered_words) 

