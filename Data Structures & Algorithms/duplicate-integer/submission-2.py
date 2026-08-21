class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = []
        for n in nums:
            if (n in current):
                return True
            else:
                current.append(n)
        return False;