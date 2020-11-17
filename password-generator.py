#!/bin/python3
import random

print('Password Length?')
length = input('--> ')
length = int(length)

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+'
for p in range(20):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)

