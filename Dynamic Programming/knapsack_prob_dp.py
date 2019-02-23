"""
__author__ = 'spati'
0/1 Knapsack problem: Given a bag which can only take certain weight W and given a list of items with their weights
and price, how do you fill this bag to maximize value of items in the bag?
"""


def knapsack(weights, values, max_bag_wt):
    """

    :param weights: List containing weights of the items
    :param values: List containing values of the items
    :param max_bag_wt: Max weight that the bag can hold
    :return: Max value and List of items(index of items) that are in the bag
    """
    # Matrix for memoization
    matrix = [[0 for _ in range(max_bag_wt+1)] for _ in range(len(values)+1)]

    # Variable to store the maximum value that can be kept in the bag
    max_val = 0

    # List containing the items (weights) that were picked
    final_list = list()

    # Fill the matrix
    for i in range(len(values)+1):
        for w in range(max_bag_wt+1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif weights[i-1] > w:
                matrix[i][w] = matrix[i-1][w]
            elif weights[i-1] <= w:
                matrix[i][w] = max(values[i-1]+matrix[i-1][w-weights[i-1]], matrix[i-1][w])

            if matrix[i][w] > max_val:
                max_val = matrix[i][w]

    # Backtrack through the matrix (bottom-up) to get the desired items
    i = len(values)
    j = max_bag_wt
    current_bag_wt = 0
    while i > 0 and j > 0:
        if matrix[i][j] == matrix[i-1][j]:
            i -= 1
        else:
            final_list.append(i-1)
            current_bag_wt += weights[i-1]
            if current_bag_wt == max_bag_wt:
                break
            i -= 1
            j = j-weights[i-1]
    return max_val, final_list[::-1]


# val_arr = [60, 100, 120]
# wt_arr = [10, 20, 30]
# max_wt = 50
wt_arr = [1, 3, 4, 5]
val_arr = [1, 4, 5, 7]
max_wt = 7
final_val, bag_list = knapsack(wt_arr, val_arr, max_wt)
print("Max Val: {}".format(str(final_val)))
print("Printing items in the bag: ")
print(bag_list)

