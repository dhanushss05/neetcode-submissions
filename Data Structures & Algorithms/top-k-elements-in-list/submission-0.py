import collections
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count frequencies automatically
        count = collections.Counter(nums)
        
        # Return the k keys with the largest values (frequencies)
        return heapq.nlargest(k, count.keys(), key=count.get)