#!/usr/bin/python3
for number in range(97, 123):
    if (number != 101 and number != 113):
        print('{:c}'.format(number), end='')
