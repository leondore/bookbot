#! python3


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    return chars


def sort_by_amount(item):
    return item[1]


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    count = count_words(file_contents)
    chars = list(count_chars(file_contents).items())
    chars.sort(key=sort_by_amount, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")
    for char in chars:
        print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")


main()
