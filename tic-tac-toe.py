# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:48:21 2020

@author: OKS-8
"""

def check_the_rows(matrix):
    flag = False
    global winer
    winer = None
    for row in matrix:
        inline = 0
        for index in range(len(row)):
            if row[index] == row[index-1]:
                inline += 1
        if inline == 3 and row[index] != '_':
            if winer != None:
                winer = 'both'
                return False
#            global winer
            winer = row[index]
            flag = True
    return flag

def check_the_column(matrix):
    flag = False
    global winer
    winer = None
    for index in range(len(matrix[0])):
        inline = 0
        for j in range(len(matrix)):
            if matrix[j][index] == matrix[j-1][index]:
                inline += 1
        if inline == 3 and matrix[j][index] != '_':
            if winer != None:
                winer = 'both'
                return False
#            global winer
            winer = matrix[j][index]
            flag = True
    return flag

def check_the_diagonal(matrix):
    if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]) or (matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]) and matrix[1][1] != '_':
        global winer
        winer = matrix[1][1]
        return True
    return False

def check_the_empty(matrix):
    for row in matrix:
        if '_' in row:
            return False
    return True

def check_number(matrix):
    x = 0
    o = 0
    for row in matrix:
        for index in row:
            if index == 'X':
                x += 1
            elif index == 'O':
                o += 1
    if abs(x - o) > 1:
        return True
    return False

def check_the_game(matrix):
    if check_the_rows(matrix) or check_the_column(matrix) or check_the_diagonal(matrix):
        print(f'{winer} wins')
    elif check_the_empty(matrix):
        print('Draw')
    elif check_number(matrix) or winer == 'both':
        print('Impossible')
    else:
        return 'Game not finished'
    
def print_the_game(matrix):
        print('---------' + '\n'
          '| ' + ' '.join(matrix[0]) + ' |' + '\n'
          '| ' + ' '.join(matrix[1]) + ' |' + '\n'
          '| ' + ' '.join(matrix[2]) + ' |' + '\n'
          '---------'
          )

def translate_coordinates(matrix, col, row):
    dct_col = {1:0, 2:1, 3:2}
    dct_row = {1:2, 2:1, 3:0}
    if matrix[dct_row[row]][dct_col[col]] == '_':
        matrix[dct_row[row]][dct_col[col]] = 'X'
        global flag
        flag = True
    else:
        print('This cell is occupied! Choose another one!')
    return matrix
    
def start_the_game():
    inp = input('Enter cells: ')
    first_line = [inp[i] for i in range(0, 3)]
    second_line = [inp[i] for i in range(3, 6)]
    third_line = [inp[i] for i in range(6, 9)]
    matrix = [first_line, second_line, third_line]    
    print_the_game(matrix)
    global flag
    flag = False
#    while check_the_game(matrix) == 'Game not finished':
    while flag == False:
        try:
            col, row = map(int, input('Enter the coordinates: ').split())
            translate_coordinates(matrix, col, row)
        except ValueError:
            print('You should enter numbers!')
        except KeyError:
            print('Coordinates should be from 1 to 3!')
    print_the_game(matrix)
                
start_the_game()








