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
    subarray_sum = []
    for i in range(len(nums)):
        subarray_sum.append((sum(nums[i:k])))
        i += 1
        k += 1
    return max(subarray_sum)
