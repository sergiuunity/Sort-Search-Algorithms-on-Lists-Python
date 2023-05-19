import random

MAX_SIZE = 100

# different lambda functions for comparing elements in an array
# increasing numbers
increasing_numbers = lambda first, second: first <= second
# decreasing numbers
decreasing_numbers = lambda first, second: first >= second


# generates a list of given size with random numbers from 1 to MAX_SIZE
def generate_random_list(size):
    result = []
    for i in range(size):
        result.append(random.randint(1, MAX_SIZE))
    return result


# sorts a given list of numbers based on the given criterion using Bubble Sort and returns it
def bubble_sort(given_list, criterion):
    for i in range(len(given_list)):
        for j in range(len(given_list) - 1):
            if not criterion(given_list[j], given_list[j + 1]):
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
    return given_list


if __name__ == '__main__':
    given_size = 50
    my_list = generate_random_list(given_size)
    print(my_list)
    my_list = bubble_sort(my_list, increasing_numbers)
    print(my_list)
