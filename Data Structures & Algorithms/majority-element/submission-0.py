class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapped = {}
        for n in nums:
            if n in mapped:
                mapped[n] += 1
            else: mapped[n] = 1
        maxnum = max(mapped.values())
        for key, value in mapped.items():
            if value == maxnum: return key
        return 0