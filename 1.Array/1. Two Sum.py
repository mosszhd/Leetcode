from os import PRIO_PGRP
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = dict()
        for i,num in enumerate(nums):
            val = target - num
            if val in track.keys():
                return [track[val],i]
            else:
                track[num] = i

sol = Solution()
print(sol.twoSum([3,2,4],5))
