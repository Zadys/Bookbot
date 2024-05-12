def main(): 
    print_report("books/frankenstein.txt")

def get_file_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_letter_dict(text):
    letter_dict = {}
    for c in text:
        c = c.lower()
        if(not c.isalpha()):
            continue
        if(c not in letter_dict):
            letter_dict[c] = 1
        else:
            letter_dict[c] += 1
    return letter_dict

def sort_on(dict):
    return dict["value"]

def convert_dict_to_list(dict):
    list = []
    for k in dict:
        list.append({"key":k, "value":dict[k]})
    return list
        

def print_report(file_path):
    text = get_file_text(file_path)
    word_count = get_word_count(text)
    letter_dict = get_letter_dict(text)
    print(f"\n=================== Begin report of {file_path} ===================\n")
    print(f"There are {word_count} words in this book.\n")
    temp_list = convert_dict_to_list(letter_dict)
    temp_list.sort(reverse=True, key=sort_on)
    for dict in temp_list:
        print(f"The letter {dict["key"]} appeared {dict["value"]} times")
    print(f"\n=================== End report of {file_path} ===================")
    

main()