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


# returns True if the given list is sorted according to the given criterion and False otherwise
# Time Complexity: O(n)
def is_sorted(given_list, criterion):
    for i in range(len(given_list) - 1):
        if not criterion(given_list[i], given_list[i + 1]):
            return False
    return True


# sorts a given list of numbers based on the given criterion using Bubble Sort and returns it
# Time Complexity: O(n^2)
def bubble_sort(given_list, criterion):
    for i in range(len(given_list)):
        for j in range(len(given_list) - 1):
            if not criterion(given_list[j], given_list[j + 1]):
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
    return given_list


# sorts a given list of numbers based on the given criterion using Bubble Sort and returns it
# Time Complexity: O()
def insertion_sort(given_list, criterion):
    for i in range(1, len(given_list)):
        j = i
        while not criterion(given_list[j - 1], given_list[j]) and j > 0:
            given_list[j - 1], given_list[j] = given_list[j], given_list[j - 1]
            j = j - 1
    return given_list


if __name__ == '__main__':
    given_size = 50
    my_list = generate_random_list(given_size)
    print(my_list)
    # my_list = bubble_sort(my_list, increasing_numbers)
    my_list = insertion_sort(my_list, decreasing_numbers)
    print(my_list)
    print(is_sorted(my_list, decreasing_numbers))
