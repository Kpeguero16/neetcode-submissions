class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            wordMap = {}
            for c in word:
                if c in wordMap:
                    wordMap[c] += 1
                else:
                    wordMap[c] = 1
            result[tuple(sorted(wordMap.items()))].append(word)
        return list(result.values())

