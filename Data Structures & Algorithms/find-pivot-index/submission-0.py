class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefixSum[i] = nums[i]
            else:
                prefixSum[i] = prefixSum[i-1] + nums[i]
        
        for i in range(len(nums)):
            leftSum = prefixSum[i-1] if i!= 0 else 0
            rightSum = prefixSum[len(nums) - 1] - prefixSum[i] if i != len(nums) else 0
            if leftSum == rightSum: 
                return i
        
        return -1