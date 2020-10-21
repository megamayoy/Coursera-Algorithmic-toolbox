# Uses python3
import sys
import itertools


def construct_matrix(sum, number_of_souvenirs):

    target_size = int(sum/3)
    dp_matrix = [[[0 for _ in range(number_of_souvenirs + 1)]
                  for _ in range(target_size+1)] for _ in range(target_size+1)]
    for i in range(number_of_souvenirs + 1):
        dp_matrix[0][0][i] = 1
    return dp_matrix


def can_partition(souvenir_amounts):
    target_size = int(sum(souvenir_amounts)/3)
    number_of_souvenirs = len(souvenir_amounts)
    dp_matrix = construct_matrix(sum(souvenir_amounts), number_of_souvenirs)
    # print(dp_matrix)
    for i in range(0, target_size+1):
        for j in range(0, target_size+1):
            for k in range(0, number_of_souvenirs + 1):
                if i == 0 and j == 0:
                    continue
                if souvenir_amounts[k-1] > i:
                    dp_matrix[i][j][k] = (
                        dp_matrix[i][j][k-1]
                        or dp_matrix[i][j-souvenir_amounts[k-1]][k-1]
                    )
                elif souvenir_amounts[k-1] > j:
                    dp_matrix[i][j][k] = (
                        dp_matrix[i][j][k-1]
                        or dp_matrix[i-souvenir_amounts[k-1]][j][k-1]
                    )
                else:
                    dp_matrix[i][j][k] = (
                        dp_matrix[i][j][k-1]  # leave
                        # take in first sack
                        or dp_matrix[i-souvenir_amounts[k-1]][j][k-1]
                        # take it in second sack
                        or dp_matrix[i][j-souvenir_amounts[k-1]][k-1]
                    )
    return dp_matrix[target_size][target_size][number_of_souvenirs]


if __name__ == '__main__':
    _ = int(input())
    souvenirs_amounts = list(map(int, input().split()))
    total_sum = sum(souvenirs_amounts)
    can_be_partitioned = 0
    if total_sum % 3 == 0:
        can_be_partitioned = can_partition(souvenirs_amounts)

    print(can_be_partitioned)
