import sys

word = sys.stdin.readline().rstrip()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for s in croatia:
    word = word.replace(s, '*')

print(len(word))