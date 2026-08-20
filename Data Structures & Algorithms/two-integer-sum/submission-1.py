class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Loop through each index
        for i in range(len(nums)):
            # Loop through the remaining indices to the right of 'i'
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return the indices directly