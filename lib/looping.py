#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
        print('Happy New Year!')


def square_integers(int_list):
    # code goes here!
    int_list = [list ** 2 for list in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    for x in range(1, 101):
        if (x % 3 == 0 and x % 5 == 0):
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)