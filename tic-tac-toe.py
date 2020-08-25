# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:48:21 2020

@author: OKS-8
"""

'''
Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os.
Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place. 
One of the players plays as 'X', and the other player is 'O'. 'X' plays first, then the 'O' side plays, and so on.
The first player that writes 3 'X' or 3 'O' in a straight line (including diagonals) wins.

Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) 
like in this table:
(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)

How to use:
    Run the file in IDE or CLI.
    The game asks to enter coordinates and shows the 3x3 field:
        'X' start the game.
        input: two numbers divided by space from 1 to 3.
        output: the state of the game and maybe offer for enter coordinates again.
        
Possible states of the game:
"Game not finished" when no side has a three in a row but there are still empty cells;
"Draw" when no side has a three in a row and there are no empty cells left;
"X wins" when the field has three Xs in a row;
"O wins" when the field has three Os in a row;
"Impossible" when the field has three Xs in a row as well as three Os in a row. 
Or the field has a lot more Xs that Os or vice versa (if the difference is 2 or more, should be 1 or 0). 

Possible error-messages:
-"This cell is occupied! Choose another one!" if the cell is not empty;
-"You should enter numbers!" if the user enters other symbols instead of numbers;
-"Coordinates should be from 1 to 3!" if the user goes beyond the field.
'''

def check_the_rows(matrix):
    '''
    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    boolean False or winer
        It's hard to explain...
    '''
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
            winer = row[index]
    return winer

def check_the_column(matrix):
    '''
    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    boolean False or winer
        It's hard to explain...
    '''
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
            winer = matrix[j][index]
    return winer

def check_the_diagonal(matrix):
    '''
    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    boolean
    '''
    if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]) or (matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]):
        if matrix[1][1] != '_':
            global winer
            winer = matrix[1][1]
            return True
    return False

def check_the_empty(matrix):
    '''
    Function finds out empty cells. If there is - returns True, else - False
    
    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    bool
    '''
    for row in matrix:
        if '_' in row:
            return False
    return True

def check_number(matrix):
    '''
    The function checks the number of noughts and crosses. Their ratio should be less than two.

    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    bool
    '''
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
    '''
    The function checks wheather the game is over.

    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    str or print(built-in function)
        It's hard to explain...

    '''
    if check_the_rows(matrix) or check_the_column(matrix) or check_the_diagonal(matrix):
        print(f'{winer} wins')
    elif check_the_empty(matrix):
        print('Draw')
    elif check_number(matrix) or winer == 'both':
        print('Impossible')
    else:
        return 'Game not finished'
    
def print_the_game(matrix):
    '''
    Prints out the field of the game.

    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    None. Just print

    '''
    print('---------' + '\n'
          '| ' + ' '.join(matrix[0]) + ' |' + '\n'
          '| ' + ' '.join(matrix[1]) + ' |' + '\n'
          '| ' + ' '.join(matrix[2]) + ' |' + '\n'
          '---------'
          )

def translate_coordinates(matrix, col, row):
    '''
    Fills the empty cell with the value.

    Parameters
    ----------
    matrix : a list
        list with 3 elements: 'X', 'O' or '_'.

    Returns
    -------
    a list
    '''
    dct_col = {1:0, 2:1, 3:2}
    dct_row = {1:2, 2:1, 3:0}
    if matrix[dct_row[row]][dct_col[col]] == '_':
        matrix[dct_row[row]][dct_col[col]] = now
        global flag
        flag = True
    else:
        print('This cell is occupied! Choose another one!')
    return matrix
    
def start_the_game():
    first_line = ['_' for i in range(0, 3)]
    second_line = ['_' for i in range(3, 6)]
    third_line = ['_' for i in range(6, 9)]
    matrix = [first_line, second_line, third_line]    
    print_the_game(matrix)
    global now, then
    now, then = 'X', 'O'
    while check_the_game(matrix) == 'Game not finished':
        try:
            col, row = map(int, input('Enter the coordinates: ').split())
            translate_coordinates(matrix, col, row)
        except ValueError:
            print('You should enter numbers!')
        except KeyError:
            print('Coordinates should be from 1 to 3!')
        print_the_game(matrix)
        now, then = then, now
                
start_the_game()








