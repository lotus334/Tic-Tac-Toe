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
    inline = 0
    for index in range(len(matrix[0])):
        for row in matrix:
            if row[index] == row[index - 1]:
                inline += 1
        if inline == 3:
            global winer
            winer = row[index]
            return True
    return False

print(matrix)

if check_the_rows(matrix) or check_the_column(matrix):
    print(f'{winer} wins')
else:
    print('None')