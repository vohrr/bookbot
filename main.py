
def main(filepath:str):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        letter_dictionary = create_dictionary(file_contents)
        print_report(word_count, letter_dictionary, filepath)

def get_word_count(contents:str):
    return len(contents.split())

def create_dictionary(contents:str):
    lower_string = contents.lower()
    letter_dictionary = dict()
    for index in lower_string:
        if index in letter_dictionary:
            letter_dictionary[index] += 1
        else: 
            letter_dictionary[index] = 1
    return letter_dictionary

def sort_on(letter_dictionary:dict):
    return letter_dictionary[1]

def print_report(word_count:int, letter_dictionary:dict, filepath:str):
    letter_list:list = []
    for letter in letter_dictionary:
        if str(letter).isalpha():
            letter_list.append([letter, letter_dictionary[letter]])
    letter_list.sort(reverse=True,key = lambda x: x[1])
    
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document")
    for letter in letter_list:
        print(f"The {letter[0]} character was found {letter[1]} times")
    print("--- End Report ---")



main("books/frankenstein.txt")
