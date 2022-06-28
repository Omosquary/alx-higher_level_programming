#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end="")

if number < 0:
    last_num = number % -10
else:
    last_num = number % 10

if last_num > 5:
    print("{:d} and is greater than 5".format(last_num))
elif last_num == 0:
    print("{:d} and is 0".format(last_num))
else:
    print("{:d} and is less than 6 and not 0".format(last_num))
