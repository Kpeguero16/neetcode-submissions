class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1];
        new_target = -11000000
        for i in range(0, len(nums)):
            if target - nums[i] in nums:
                new_target = target - nums[i]
                for j in range(i+1, len(nums)):
                    if nums[j] == new_target:
                        return [i, j]