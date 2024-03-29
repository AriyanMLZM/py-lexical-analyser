"""
Ariyan Molazem
Lexical Analyser
GUI
"""

from tkinter import *
import os
from msvcrt import getch

# Global variables:
next_state = 0
final_state = -1
symbol_tbl = dict()
s_count = 0
tokens = ""

# The function of each state of dfa:
def state_0(char):
    global next_state
    global final_state
    if char == ' ':
        next_state = 0
    elif char == '\n':
        next_state = 0
    elif char.isalpha():
        next_state = 1
    elif char == '+':
        next_state = 2
    elif char == '-':
        next_state = 3
    elif char.isnumeric():
        next_state = 4
    elif char == '(':
        next_state = 7
    elif char == ')':
        next_state = 8
    elif char == ';':
        next_state = 9
    elif char == '{':
        next_state = 10
    elif char == '}':
        next_state = 11
    elif char == '/':
        next_state = 12
    elif char == '"':
        next_state = 18
    elif char == '*':
        next_state = 20
    elif char == '=':
        next_state = 21
    elif char == '<':
        next_state = 23
    elif char == '>':
        next_state = 25
    elif char == '!':
        next_state = 27
    else:
        next_state = -1
def state_1(char):
    global next_state
    global final_state
    if char.isalnum():
        next_state = 1
    else:
        final_state = 1     
def state_2(char):
    global next_state
    global final_state
    if char.isnumeric():
        next_state = 4
    else:
        final_state = 2
def state_3(char):
    global next_state
    global final_state
    if char.isnumeric():
        next_state = 4
    else:
        final_state = 3
def state_4(char):
    global next_state
    global final_state
    if char.isnumeric():
        next_state = 4
    elif char == '.':
        next_state = 5
    else:
        final_state = 4
def state_5(char):
    global next_state
    global final_state
    if char.isnumeric():
        next_state = 6
    else:
        next_state = -1
def state_6(char):
    global next_state
    global final_state
    if char.isnumeric():
        next_state = 6
    else:
        final_state = 6
def state_7(char):
    global next_state
    global final_state
    final_state = 7
def state_8(char):
    global next_state
    global final_state
    final_state = 8
def state_9(char):
    global next_state
    global final_state
    final_state = 9
def state_10(char):
    global next_state
    global final_state
    final_state = 10
def state_11(char):
    global next_state
    global final_state
    final_state = 11
def state_12(char):
    global next_state
    global final_state
    if char == '/':
        next_state = 13
    elif char == '*':
        next_state = 15
    else:
        final_state = 12
def state_13(char):
    global next_state
    global final_state
    if char != '\n':
        next_state = 13
    else:
        next_state = 14
def state_14(char):
    global next_state
    global final_state
    final_state = 14
def state_15(char):
    global next_state
    global final_state
    if char != '*':
        next_state = 15
    else:
        next_state = 16
def state_16(char):
    global next_state
    global final_state
    if char == '*':
        next_state = 16
    elif char == '/':
        next_state = 17
    else:
        next_state = 15
def state_17(char):
    global next_state
    global final_state
    next_state = 17
def state_18(char):
    global next_state
    global final_state
    if char == '"':
        next_state = 19
    else:
        next_state = 18
def state_19(char):
    global next_state
    global final_state
    final_state = 19
def state_20(char):
    global next_state
    global final_state
    final_state = 20
def state_21(char):
    global next_state
    global final_state
    if char == '=':
        next_state = 22
    else:
        final_state = 21
def state_22(char):
    global next_state
    global final_state
    final_state = 22
def state_23(char):
    global next_state
    global final_state
    if char == '=':
        next_state = 24
    else:
        final_state = 23
def state_24(char):
    global next_state
    global final_state
    final_state = 24
def state_25(char):
    global next_state
    global final_state
    if char == '=':
        next_state = 26
    else:
        final_state = 25
def state_26(char):
    global next_state
    global final_state
    final_state = 26
def state_27(char):
    global next_state
    global final_state
    if char == '=':
        next_state = 28
    else:
        next_state = -1
def state_28(char):
    global next_state
    global final_state
    final_state = 28

# Select what state to run based on next_state:
def run_state(char):
    exec("state_" + str(next_state) + "(char)")

# Check identifiers in symbol table:
def check_symboltbl(identifier):
	global tokens
	global s_count
	if(identifier in symbol_tbl.keys()):
		tokens += ' <id, ' + str(symbol_tbl[identifier]) + '>'
	else:
		s_count += 1
		symbol_tbl[identifier] = s_count
		tokens += ' <id, ' + str(symbol_tbl[identifier]) + '>'

# Make tokens based of avtived final_state: 
def final_state_action(words):
    global tokens
    if final_state == 1:
        if words in ["chap", "agar", "begir", "sahih", "ashar", "baraye", "tavaghtike"]:
            tokens += ' <' + words + '>'
        else:
            check_symboltbl(words)
    elif final_state in [14, 17]:
        pass
    else:
        tokens += ' <' + words + '>'

# Main execute function:
def execute():
    global next_state
    global final_state
    global tokens
    flag_err = False
    with open("files/input.txt", "r") as infile:
        content = infile.read()
    content += " "
    temp = ""
    ind = 0
    while ind != len(content):
        run_state(content[ind])
        if next_state == 0:
            temp = ""
        else:
            temp += content[ind]
        if next_state == -1:
            L1.config(text = "Error: '{0}' is unvalid".format(temp))
            flag_err = True
            break
        if final_state != -1:
            temp = temp[:-1]
            final_state_action(temp)
            final_state = -1
            next_state = 0
            temp = ""
            ind -= 1
        ind += 1
    with open("files/output.txt", "w") as outfile:
        outfile.write(tokens)
    tokens = ""
    if(not flag_err):
        L1.config(text = "Tokens are created in output file")

# Open files in notepad:
def open_input():
	os.system("notepad files/input")
def open_output():
	os.system("notepad files/output")

# Tkinter methods: 
menu = Tk()
menu.geometry("350x350")
menu.title("Lexical Analyser")
menu.config(background="#222")
	
head = Label(menu, text = "Lexical Analyser", 
			bg = "#222",fg = "#5d8aa8", 
            width = 500, height=1, font = ('summer', 18))
L1 = Label(menu, relief = FLAT, bg = "#1a1a1a", fg = "#5d8aa8",
			width = 500, height = 1, font = ('summer', 14))
	
B1 = Button(menu, relief = FLAT, text = ">      Open input file      <", activeforeground = '#1a1a1a',
			activebackground = "#5d8aa8", command=open_input, bg = "#1a1a1a", fg = "#5d8aa8",
			width = 500, font = ('summer', 16))
B2 = Button(menu, relief = FLAT, text = ">           Execute           <", activeforeground = '#1a1a1a',
			activebackground = "#5d8aa8", command=execute, bg = "#1a1a1a", fg = "#5d8aa8",
			width = 500, font = ('summer', 16))	
B3 = Button(menu, relief = FLAT, text = ">     Open output file     <", activeforeground = '#1a1a1a',
			activebackground = "#5d8aa8", command=open_output, bg = "#1a1a1a", fg = "#5d8aa8",
			width = 500, font = ('summer', 16))		
B4 = Button(menu, text = "Exit", relief = FLAT, command = menu.quit, activeforeground = '#a32725',
			activebackground = "#333", bg = "#1a1a1a", fg = "#a32725",
			width = 500, font = ('summer', 16))

head.pack(side = 'top', pady=20)
B1.pack(side = "top")
B2.pack(side = "top", pady=15)
L1.pack(side = 'top')
B3.pack(side = "top", pady=15)
B4.pack(side = 'bottom')	

menu.mainloop()
