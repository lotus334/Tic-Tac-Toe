# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:48:21 2020

@author: OKS-8
"""

inp = input('Enter cells: ')

first_line = [inp[i] for i in range(0, 3)]
second_line = [inp[i] for i in range(3, 6)]
third_line = [inp[i] for i in range(6, 9)]
matrix = [first_line, second_line, third_line]

print('---------' + '\n'
      '| ' + ' '.join(first_line) + ' |' + '\n'
      '| ' + ' '.join(second_line) + ' |' + '\n'
      '| ' + ' '.join(third_line) + ' |' + '\n'
      '---------'
      )

def check_the_rows(matrix):
    for row in matrix:
        inline = 0
        for index in range(len(row)):
            if row[index] == row[index-1]:
                inline += 1
        if inline == 3 and row[index] != '_':
            global winer
            winer = row[index]
            return True
    return False

def check_the_column(matrix):
#    inline = 0
    for index in range(len(matrix[0])):
        inline = 0
        for j in range(len(matrix)):
            if matrix[j][index] == matrix[j-1][index]:
                inline += 1
        if inline == 3 and matrix[j][index] != '_':
            global winer
            winer = matrix[j][index]
            return True
    return False

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

if check_the_rows(matrix) or check_the_column(matrix) or check_the_diagonal(matrix):
    print(f'{winer} wins')
elif check_the_empty(matrix):
    print('Draw')
else:
    print('None')