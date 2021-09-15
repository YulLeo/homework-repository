from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Browsing a sub-array with length less equal to "k", with maximal sum.
    Returns the sum of this sub-array.

    Args:
        nums (list): List of integers numbers
        k (int): Sub-array length

    Returns:
        int: maximum sum of sub-array length less or equal k
    """
    sub_array_length = k
    max_sum = sum(nums[0:sub_array_length])
    for num in range(len(nums)):
        if sum(nums[num:sub_array_length]) > max_sum:
            max_sum = sum(nums[num:sub_array_length])
        sub_array_length += 1
    return max_sum
