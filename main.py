def count_words(str):
    return str.read().split()

def count_letters(str):
    dict = {}
    
    for word in str:
        for letter in word:
            letter = letter.lower()
            val = dict.get(letter)
            if val != None:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict

with open("./books/frankenstein.txt") as my_file:
    contents = count_words(my_file)
    letter_count = count_letters(contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(contents)} words found in the document\n\n")
    
    characters = []

    for item in letter_count:
        if item.isalpha():
            characters.append(item)
        
    characters = sorted(characters)

    for item in characters:
        if item in letter_count:
            print(f"The {item} character was found {letter_count[item]} times")

  


