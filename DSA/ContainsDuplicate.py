from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = [1, 2, 3, 4, 5]
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if(nums[i] == nums[j]):
                    return True
        return False