

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # avoid repeating same pair
                if nums[i] + nums[j] == target:
                    return [i, j]  # return as soon as you find the pair

obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]




a = ['Geeks', 'for', 'Geeks']

# Creating an enumerate object from the list 'a' 
b = enumerate(a)

# This retrieves the first index-element pair from 'b'
nxt_val = next(b)
print(nxt_val)


# Bonus: Faster version using a dictionary (O(n) time)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

