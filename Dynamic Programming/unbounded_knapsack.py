"""
__author__ = 'spati'
Given a knapsack weight W and a set of n items with certain value val and weight wt,
we need to calculate minimum amount that could make up this quantity exactly.
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
Find maximum achievable value.

Reference: https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
"""


def unbounded_knapsack(weights, values, max_bag_wt):
    """

    :param weights: List containing weights of the items
    :param values: List containing values of the items
    :param max_bag_wt: Max weight that the bag can hold
    :return: Maximum achievable value
    """
    # Create a 1D list
    dp_list = [0 for _ in range(max_bag_wt+1)]

    # For every possible weight of bag i, iterate through every weight of items that we have and keep storing the max
    # possible value for weight i among all the items available to us.
    for i in range(max_bag_wt+1):
        for j in range(len(weights)):
            if weights[j] <= i:
                dp_list[i] = max(dp_list[i], dp_list[i-weights[j]]+values[j])

    return dp_list[max_bag_wt]


bag_wt = 100
val = [10, 30, 20]
wt = [5, 10, 15]
print(unbounded_knapsack(wt, val, bag_wt))
