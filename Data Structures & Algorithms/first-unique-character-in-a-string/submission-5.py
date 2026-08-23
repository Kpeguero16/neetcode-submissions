class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {}
        for i in range(len(s)):
            if s[i] in charMap:
                charMap[s[i]][0] += 1
            else:
                charMap[s[i]] = [1, i]
        if not charMap: return -1
        for key in charMap:
            if charMap[key][0] == 1: 
                return int(charMap[key][1])
        return -1