import sys
from stats import get_book_text, get_num_words, get_num_characters, sort_on

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

text = get_book_text(path=path)
num_words = get_num_words(text=text)
chars = get_num_characters(text=text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
chars.sort(reverse=True, key=sort_on)
for i in chars:
    print(f"{i['char']}: {i['num']}")
print("============= END ===============")
