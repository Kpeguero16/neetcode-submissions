class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res = []
        count = 0
        for n in nums:
            if n == 0: 
                count +=1
            else:
                res.append(n)
        for i in range(0, count):
            res.append(0)
        for i in range(len(nums)):
            nums[i] = res[i]