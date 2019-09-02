from colors import *

def printc(color, *args):
    print(color)
    print(*args)
    print(c.ENDC)

def uinput(prompt: str) -> str:
    '''Display formatted prompt and return user input'''

    print("\n", prompt)
    inp = input("\n> ")
    return inp

def tfinput(prompt: str) -> bool:
    '''Return True of False based on user [Y/N] input'''

    print("\n", prompt, " Y/N")
    inp = input("\n> ").upper()
    return inp == 'Y' or inp == ''


def parsefile():
    newfile = open("./parsed_data.txt", 'w+')

    for line in lines:
        word = line.split(" ")

        newline = separator.join(word)
        newfile.write(newline)

def is_duplicate_in_file(eng_word: str) -> bool:
    file = open("./data.txt", 'r')
    lines = file.readlines()

    for line in lines:
        words = line.split("//")
        to_compare = words[0]

        if eng_word.strip() == to_compare:
            return True

def file_score(score: int, date):
    """Write a score and date entry to scoretable.txt"""

    file = open("./scoretable.txt", 'a+')
    score = str(score)

    score_num_of_digits = len(score)
    max_offset = 10
    offset = max_offset - score_num_of_digits

    score_entry = " " + score + (offset * " ") + "| " + date


    separator_len = 24
    separator = "\n" + (separator_len * "_") + "\n"
    

    file.write(score_entry)
    file.write(separator)

    file.close()
