def get_book_text(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = text.split()
    num_words = len(words)
    # print(f"{num_words} words found in the document")
    return num_words


def get_num_characters(text):
    char_counts = {}
    char_list = []
    for ch in text.lower():
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1

    for char in char_counts:
        if char.isalpha():
            char_list.append({"char":char, "num":char_counts[char]})
    return char_list

def sort_on(dict):
    return(dict["num"])

