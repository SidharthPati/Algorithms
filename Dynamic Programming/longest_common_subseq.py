# __author__ = 'spati'
import numpy as np


def longest_common_subsequence(str1, str2):
    """

    :param str1: 1st string
    :param str2: 2nd string
    :return: Longest Common Subsequence
    """
    lcs = ""
    matrix_len = len(str1)+1
    matrix_breadth = len(str2)+1

    # Create empty matrix with 0s
    matrix = np.zeros((matrix_breadth, matrix_len))

    # Memoization
    for i in range(1, matrix_breadth):
        for j in range(1, matrix_len):
            if str1[j-1] == str2[i-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    # Backtrack to get LCS
    i = matrix_breadth - 1
    j = matrix_len - 1
    while i != 0 and j != 0:
        if matrix[i-1][j] == matrix[i][j-1]:
            if str1[j-1] == str2[i-1]:
                lcs += str1[j-1]
                i = i-1
                j = j-1
            else:
                i = i-1
                j = j-1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i = i-1
        else:
            j = j-1

    # return the reversed string
    return lcs[::-1]


str_x = "abcdaf"
str_y = "acbcf"
# str_x = "abcdgh"
# str_y = "aedfhr"
# str_x = "aggtab"
# str_y = "gxtxayb"
print(longest_common_subsequence(str_x, str_y))
