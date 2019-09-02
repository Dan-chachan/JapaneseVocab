import random
import os
import time
from utilities import *
from declarations import *
from colors import *

def write_score():
    '''Writes formatted score'''

    #printc(c.DARK, "\n================")
    printc(c.LIME, "\nSCORE: ", score, "/", max_score)
    #printc(c.DARK, "\n================")

def write_separator():
    '''Prints a long separator'''

    printc(c.DARK, "============================")

def write_answer():
    '''Prints all of the word\'s variations'''

    print(c.YELLOW)
    print("\n ENGLISH: ", eng)
    print("\n HIRAGANA: ", hira)
    print("\n KANJI: ", kan)
    print(c.ENDC)

def user_choose_mode() -> list:
    '''Asks user what mode they want and returns a list'''

    clear()
    print(c.BOLD, "\n\nChoose mode:", c.ENDC)
    print("Type multiple letters for a combination")
    print(c.BOLD, end='')
    printc(c.YELLOW, "\n[E]nglish - [H]iragana - [K]anji\n")
    #print(c.ENDC)
    printc(c.YELLOW, "[D]atabase editor")
    printc(c.YELLOW, "e[X]it")
    mode = input("\n> ").upper()

    return list(mode)

mode = user_choose_mode()

# Game loop
while True:
    program_continue = True
    if ('E' in mode or 'H' in mode or 'K' in mode):
        file_data_r = open("./data.txt", 'r')
        lines = file_data_r.readlines()

        while (len(lines) > 0) and program_continue:
            line_index = random.randint(0, len(lines) - 1)

            line = lines.pop(line_index)

            word = line.split(separator)

            eng = word[0]
            hira = word[1]
            kan = word[2]


            #write_separator()
            clear()

            if 'E' in mode:
                printc(c.YELLOW, "\n", eng)
            if 'H' in mode:
                printc(c.YELLOW, "\n", hira)
            if 'K' in mode:
                printc(c.YELLOW, "\n", kan)

            input("\nPress anything to display answer")

            #write_separator()
            clear()

            write_answer()

            #write_separator()

            correct = tfinput("Did you have it right?")
            score = score + 1 if correct else score
            
            clear()
            write_score()

            if len(lines) > 0:
                program_continue = tfinput("Continue?")
            else:
                input("\nThat's all!")
        file_data_r.close()
    elif ('D' in mode):
        file_data_a = open("./data.txt", 'a+')
        prompts = ["ENGLISH:", "HIRAGANA:", "KANJI:"]
        
        while program_continue:
            clear()
            line = ""

            for i in range(0, 3):
                printc(c.YELLOW, "\n", prompts[i])
                word = input("\n> ")

                if i == 0:    
                    line += word
                    duplicate = is_duplicate_in_file(word)
                    if duplicate: break
                else:
                    line += separator + word

            if duplicate:
                printc(c.YELLOW, "This word is already present in the database, cancelling")
            
            else:
                clear()
                print("\nEntry: ")
                printc(c.LIME, "\n", line)

                isOk = tfinput("Ok?")

                if isOk:
                    printc(c.LIME, "\nWriting..")
                    line += "\n"
                    file_data_a.write(line)
                else:
                    printc(c.YELLOW, "\nCanceled")

            program_continue = tfinput("Continue?")

        file_data_a.close()
    elif ('X' in mode):
        break
    else:
        printc(c.SALMON ,"\nUnknown mode, try again")
        time.sleep(2)

    printc(c.DARK, "Saving..")
    mode = user_choose_mode()


clear()

print("\n\nBye..")
file_score(score, today_format)
#time.sleep(1)

clear()