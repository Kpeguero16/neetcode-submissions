class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = word1 + word2
        result = ""
        p1 = 0
        p2 = len(word1)
        for _ in range(max(len(word1), len(word2))):
            if p1 < len(word1):
                result += combined[p1]
            if p2 < len(combined):
                result += combined[p2]
            p1 += 1
            p2 += 1
        return result