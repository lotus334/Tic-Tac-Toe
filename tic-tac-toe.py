# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:48:21 2020

@author: OKS-8
"""

first_line = []
second_line = []
third_line = []

inp = input('Enter cells: ')

for element in range(0,3):
    first_line.append(inp[element])
for element in range(3,6):
    second_line.append(inp[element])
for element in range(6,9):
    third_line.append(inp[element])

print('---------')
print('| ' + ' '.join(first_line) + ' |')
print('| ' + ' '.join(second_line) + ' |')
print('| ' + ' '.join(third_line) + ' |')
print('---------')


'''
print('|' + ''join.O _ O |
| X X O |
| _ X X |
---------
'''