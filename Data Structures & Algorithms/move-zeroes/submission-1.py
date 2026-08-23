class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res = []
        for n in nums:
            if n != 0:
                res.append(n)
        for i in range(len(nums)):
            if i < len(res):
                nums[i] = res[i]
            else: 
                nums[i] = 0
