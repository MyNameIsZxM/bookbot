from stats import *
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        print(file_contents)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_of_words()
    print("--------- Character Count -------")
    sorted_list()
    print("============= END ===============")