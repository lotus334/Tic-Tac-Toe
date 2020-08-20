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
    for line in matrix:
        inline = 1
        for index in range(len(line)):
            if line[index] == line[index-1]:
                inline += 1
        if inline >= 3 and line[index] != '_':
            global winer
            winer= line[index]
            return True
    return False

print(matrix)

if check_the_rows(matrix) == True:
    print(f'{winer} wins')
else:
    print('None')