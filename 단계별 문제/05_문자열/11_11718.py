import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    print(line, end='')
    # while 은 돌고나서 자동으로 \n 을 하나보다,,,?
