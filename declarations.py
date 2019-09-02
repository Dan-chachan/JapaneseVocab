import datetime
import os

file = open("./data.txt", 'r')

lines = file.readlines()

separator = "//"

today = datetime.datetime.today()
today_format = today.strftime("%d-%m-%Y")

score = 0
max_score = len(lines)

program_continue = True

clear = lambda: os.system('clear')
