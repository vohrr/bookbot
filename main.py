
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(get_word_count(file_contents))

def get_word_count(contents):
    return len(contents.split())

main()
