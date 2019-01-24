# __author__ = 'spati'


def merge_sort(unsorted_list):
    """

    :param unsorted_list: Unsorted list
    :return: Does not return anything. Changes are made in unsorted_list itself
    """
    # Stop if length of the list is 1
    if len(unsorted_list) > 1:

        # find the mid point
        mid = len(unsorted_list) / 2
        left = unsorted_list[:mid]  # left half
        right = unsorted_list[mid:]  # right half

        # call the function merge_sort for both these halves
        merge_sort(left)
        merge_sort(right)

        # once the halves are divided completely, start sorting
        i = j = k = 0  # indices

        # sort by comparing an element each from both the halves
        # length of i and j should be less than the lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_list[k] = left[i]
                i = i + 1
            else:
                unsorted_list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            unsorted_list[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            unsorted_list[k] = right[j]
            j = j + 1
            k = k + 1


unsorted_list = [534, 246, 933, 127, 277, 321, 454, 565, 220]
merge_sort(unsorted_list)
print(unsorted_list)