class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        sMap = {}
        for c in s:
            if c in sMap: 
                sMap[c] += 1
            else:
                sMap[c] = 1
        tMap = {}
        for c in t:
            if c in tMap: 
                tMap[c] += 1
            else:
                tMap[c] = 1
        if len(sMap) == len(tMap):
            for key in sMap:
                if key not in tMap:
                    return False
                elif sMap[key] != tMap[key]:
                    return False
            return True
        else: return False

