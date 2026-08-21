class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        s = sorted(s)
        t = sorted(t)
        for c in range(0, len(s)):
            if (s[c] != t[c]): return False
        return True
