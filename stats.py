import sys

def num_of_words():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"Found {num_words} total words")

def count_characters():
    with open(sys.argv[1]) as f:
        file_contents = f.read().lower()
        char_counts = {}
    for char in file_contents:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    print(char_counts)

def sorted_list():
    with open(sys.argv[1]) as f:
        file_contents = f.read().lower()
        char_counts = {}
    for char in file_contents:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char in char_counts:
        if char.isalpha() == True:
            print(f"{char}: {char_counts[char]}")
        