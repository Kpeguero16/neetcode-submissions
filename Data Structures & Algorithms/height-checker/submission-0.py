class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct = sorted(heights)
        res = 0
        for i in range(len(heights)):
            res += 1 if correct[i] != heights[i] else 0
        return res