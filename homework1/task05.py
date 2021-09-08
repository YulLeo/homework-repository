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
    max_sum = sum(nums[0:k])
    for i in range(len(nums)):
        if sum(nums[i:k]) > max_sum:
            max_sum = sum(nums[i:k])
        k += 1
    return max_sum
