from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurance = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            occurance[i] = 1 + occurance.get(i,0)
        print(occurance)
        for key,value in occurance.items():
            freq[value].append(key)
        item = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                item.append(n)
                if len(item) == k:
                    return item

sol = Solution()
print(sol.topKFrequent(nums = [1], k = 1))