from stats import * 
import sys


def main(filepath:str):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        letter_dictionary = create_dictionary(file_contents)
        print_report(word_count, letter_dictionary, filepath)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])
