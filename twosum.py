class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            substitute = target - nums[i]
            for j in range(len(nums)):
                if substitute == nums[j]:
                    if not i == j:
                        return [i, j]
