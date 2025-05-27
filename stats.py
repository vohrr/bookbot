
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
    print(f"Found {word_count} total words")
    for letter in letter_list:
        print(f"{letter[0]}: {letter[1]}")
    print("--- End Report ---")
