#!/usr/bin/python3
for character in range(ord('z'), ord('a'), -2):
    print('{:c}{:c}'.format(character, (character - 33)), end='')
