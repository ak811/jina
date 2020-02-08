import random
from math import *
from random import randint

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross_in_tray_function(x, y):
    return -0.0001 * pow(abs(sin(x) * sin(y) * exp(abs(100 - (sqrt(x * x + y * y) / pi)))) + 1, 0.1)


def simulated_annealing(current):
    for temperature in reversed(range(0, T)):

        if temperature == 0:
            return current

        next = produce_random_successor_of_current(current)

        delta_e = abs(cross_in_tray_function(next.x, next.y)) - abs(cross_in_tray_function(current.x, current.y))

        if delta_e >= 0:
            current = next
        else:
            random_number = randint(0, 100)
            probability = exp(delta_e / temperature)
            if random_number < probability:
                current = next


def produce_random_successor_of_current(current):
    successor = current

    change_x_or_change_y_or_change_both = randint(0, 2)

    start = 0.8
    end = 1.2

    if change_x_or_change_y_or_change_both == 0:
        successor.x *= random.uniform(start, end)
    elif change_x_or_change_y_or_change_both == 1:
        successor.y *= random.uniform(start, end)
    elif change_x_or_change_y_or_change_both == 2:
        successor.x *= random.uniform(start, end)
        successor.y *= random.uniform(start, end)

    return successor


def produce_random_node():
    left = r1
    right = r2
    return Node(random.uniform(left, right), random.uniform(left, right))


r1 = int(input("Enter the left range of x and y: "))
r2 = int(input("Enter the right range of x and y: "))
T = int(input("Enter the start temperature: "))

current = produce_random_node()

bestNode = simulated_annealing(current)
x = bestNode.x
y = bestNode.y
print("x = " + str(x))
print("y = " + str(y))
print("F(x,y) = " + str(cross_in_tray_function(x, y)))
