from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    subarray_sum = []
    for i in range(len(nums)):
        subarray_sum.append((sum(nums[i:k])))
        i += 1
        k += 1
    return max(subarray_sum)
