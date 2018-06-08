import os

file = 'sample.py.xlsx'

path = os.path.splitext(file)
print(path[0])
print(path[1])
