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


# sorts a given list of numbers based on the given criterion using Bubble Sort and returns the resulted list
# Time Complexity: O(n^2)
def bubble_sort(given_list, criterion):
    for i in range(len(given_list)):
        for j in range(len(given_list) - 1):
            if not criterion(given_list[j], given_list[j + 1]):
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
    return given_list


# sorts a given list of numbers based on the given criterion using Insertion Sort and returns the resulted list
# Time Complexity: O()
def insertion_sort(given_list, criterion):
    for i in range(1, len(given_list)):
        j = i
        while not criterion(given_list[j - 1], given_list[j]) and j > 0:
            given_list[j - 1], given_list[j] = given_list[j], given_list[j - 1]
            j = j - 1
    return given_list


# sorts a given list of numbers based on the given criterion using Selection Sort and returns the resulted list
# Time Complexity: O(n^2)
def selection_sort(given_list, criterion):
    for i in range(len(given_list) - 1):
        crt_extreme_index = i
        for j in range(i + 1, len(given_list)):
            if not criterion(given_list[crt_extreme_index], given_list[j]):
                crt_extreme_index = j
        given_list[i], given_list[crt_extreme_index] = given_list[crt_extreme_index], given_list[i]
    return given_list


# sorts a given list of numbers based on the given criterion using Merge Sort and returns the resulted list
# Time Complexity: O()
def merge_sort(given_list, criterion):
    if len(given_list) <= 1:
        return given_list
    # split the list in 2 roughly equally-sized parts
    first_part = given_list[:len(given_list) // 2]
    second_part = given_list[len(given_list) // 2:]

    # call the method for the two lists
    first_part = merge_sort(first_part, criterion)
    second_part = merge_sort(second_part, criterion)

    # merge the two resulted lists into one
    return merge(first_part, second_part, criterion)


# merges two sorted lists into one sorted list based on the given criterion
def merge(given_list1, given_list2, criterion):
    result = []
    # adding the elements in order
    while (not not given_list1) and (not not given_list2):  # while first and second lists both have elements
        if criterion(given_list1[0], given_list2[0]):
            result.append(given_list1[0])
            given_list1.pop(0)
        else:
            result.append(given_list2[0])
            given_list2.pop(0)
    # adding remaining elements from the first list
    while not not given_list1:  # while the first list is not empty
        result.append(given_list1[0])
        given_list1.pop(0)
    # adding remaining elements from the second list
    while not not given_list2:  # while the second list is not empty
        result.append(given_list2[0])
        given_list2.pop(0)
    return result


# sorts a given list of numbers based on the given criterion using Quick Sort and returns the resulted list
# Time Complexity: O()
def quick_sort(given_list, criterion):
    if len(given_list) <= 1:
        return given_list
    first_part = []
    second_part = []
    # taking the last element as the pivot point
    pivot = given_list.pop()
    for i in range(len(given_list)):
        if criterion(given_list[i], pivot):
            first_part.append(given_list[i])
        else:
            second_part.append(given_list[i])
    return quick_sort(first_part, criterion) + [pivot] + quick_sort(second_part, criterion)


if __name__ == '__main__':
    given_size = 50
    my_list = generate_random_list(given_size)
    print(my_list)
    # my_list = bubble_sort(my_list, increasing_numbers)
    # my_list = insertion_sort(my_list, decreasing_numbers)
    # my_list = selection_sort(my_list, increasing_numbers)
    # my_list = merge_sort(my_list, increasing_numbers)
    my_list = quick_sort(my_list, decreasing_numbers)

    print(my_list)
    print(is_sorted(my_list, decreasing_numbers))
