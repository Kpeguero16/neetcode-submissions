class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
            else:
                seen[s[i]] = -1
        if not seen: return -1
        for key in seen:
            if seen[key] >= 0:
                return seen[key] 
        return -1