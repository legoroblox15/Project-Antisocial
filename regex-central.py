#!/usr/bin/env python3

import re
import skilstak.colors as cl

B03 = cl.base03
B02 = cl.base02
B01 = cl.base01
B00 = cl.base00
B0 = cl.base0
B1 = cl.base1
B2 = cl.base2
B3 = cl.base3
Y = cl.yellow
O = cl.orange
R = cl.red
MT = cl.magenta
P = cl.violet
BL = cl.blue
CY = cl.cyan
G = cl.green
RT = cl.reset
CR = cl.clear

def basic():
    while True:
        print('What do you need to learn about?\n[1] Flags\n[2] Anchors\n[3] Quantifiers\n[4] Groups and Ranges\n[5] Character Classes\n[6] Syntax Charachers\n[7] I would like to go back in time.')
        command = input('>>> ')
        if command == '1' or command == 'a':
            print(CR,end='')
        elif command == '2' or command == 'b':
            print(CR,end='') 
        elif command == '3' or command == 'c':
            print(CR,end='')
        elif command == '4' or command == 'd':
            print(CR,end='')
        elif command == '5' or command == 'e':
            print(CR,end='')
        elif command == '6' or command == 'f':
            print(CR,end='')
        elif command == '7' or command == 'g':
            print(CR,end='')
            break
        else:
            print(CR,end='')

def advanced():
    pass

while True:
    print('Welcome to Regex Central! Your personal Regex teacher.\n[1] I would like to play Regex Golf!\n[2] I would like to see a tutorial.\n[3] I would like to go back in time.')
    command = input('>>> ').strip().lower()

    if 'c' == command or '3' == command:
        print(CR,end='')
        break
    elif 'b' == command or '2' == command:
        print(CR,end='')
        while True:
            print('Basic or Advanced?\n[1] Basic\n[2] Advanced\n[3] I would like to go back in time.')
            command = input('>>> ')
            if command == '1' or command == 'a':
                print(CR,end='')
                basic()
            elif command == '2' or command == 'b':
                print(CR,end='')
                advanced()
            elif command == '3' or command == 'c':
                print(CR,end='')
                break
            else:
                print(CR,end='')
    elif 'a' == command or '1' == command:
        print(CR,end='')
    else:
        print(CR,end='')
