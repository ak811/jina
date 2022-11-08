__author__ = 'ak811'
__date__ = 'Spring 2019'

import random
from math import *
from random import randint


class Individual(object):
    # an individual has two chromosomes (x and y)
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross_in_tray_function(x, y):
    return -0.0001 * pow(abs(sin(x) * sin(y) * exp(abs(100 - (sqrt(x * x + y * y) / pi)))) + 1, 0.1)


def find_best_individual(population):
    best_individual_index = 0
    min = cross_in_tray_function(population[best_individual_index].x, population[best_individual_index].y)
    for i in range(0, len(population)):
        result = cross_in_tray_function(population[i].x, population[i].y)
        if result < min:
            min = result
            best_individual_index = i

    return best_individual_index


def genetic_algorithm(population, fitness_function):
    mutation_probability_percent = 10

    for i in range(0, generation_count):
        new_population = []
        for j in range(0, len(population)):
            father = random_selection(population, fitness_function)
            mother = random_selection(population, fitness_function)
            child = produce_child(father, mother)

            if randint(0, 100) < mutation_probability_percent:
                child = mutate_child(child)

            new_population.append(child)

        population = new_population

    return population[find_best_individual(population)]


def fitness(population):
    fitness_values = []
    fitness_percents = []

    # Cross-in-Tray function always returns negative value.
    sum = 0
    for i in range(0, len(population)):
        fitness_values.append(cross_in_tray_function(population[i].x, population[i].y))
        sum += fitness_values[i]

    for i in range(0, len(population)):
        fitness_percents.append(fitness_values[i] / sum * 100)

    return fitness_percents


def random_selection(population, fitness_percents):
    random_number = randint(0, 100)

    sum = 0
    selected_individual = population[0]
    for i in range(0, len(population)):
        sum += fitness_percents[i]
        if random_number < sum:
            selected_individual = population[i]
            break

    return selected_individual


def produce_child(father, mother):
    random_number = randint(0, 1)

    if random_number == 0:
        x = father.x
        y = mother.y
    else:
        x = mother.x
        y = father.y

    return Individual(x, y)


def mutate_child(child):
    x_or_y = randint(0, 1)
    random_float = random.uniform(0.9, 1.1)

    if x_or_y == 0:
        child.x *= random_float
    else:
        child.y *= random_float

    return child


generation_count = int(input("Enter the generation count: "))
population_count = int(input("Enter the population count: "))

population = []
for i in range(0, population_count):
    population.append(Individual(random.uniform(-10, 10), random.uniform(-10, 10)))

best_individual = genetic_algorithm(population, fitness(population))

x = best_individual.x
y = best_individual.y
print("x= " + str(x))
print("y= " + str(y))
print("F(x,y)= " + str(cross_in_tray_function(x, y)))
