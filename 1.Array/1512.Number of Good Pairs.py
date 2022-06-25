from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        count_dict = defaultdict()
        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count += count_dict[i]
                count_dict[i] += 1
        return count

sol = Solution()
ans = sol.numIdenticalPairs([1,1,1,1])

print(ans)