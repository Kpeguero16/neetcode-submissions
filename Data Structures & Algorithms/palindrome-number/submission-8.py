class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False
        num = str(x)
        p1, p2 = 0, len(num)-1
        while p1 != p2 and p1 < len(num):
            if num[p1] != num[p2]: 
                return False
            p1 += 1
            p2 = p2 - 1
        return True