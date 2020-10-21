# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    # get the the largest number in the list
    max_index_1 = 0
    max_number_1 = numbers[0]
    for index in range(1, n):
        if numbers[index] > max_number_1:
            max_index_1 = index
            max_number_1 = numbers[index]
    # set first max number to -1 in the list
    numbers[max_index_1] = -1
 
    # get the second larget number in the list
    max_number_2 = numbers[0]
    for index in range(1, n):
        if numbers[index] > max_number_2:
            max_number_2 = numbers[index]

    return max_number_1 * max_number_2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
