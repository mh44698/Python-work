class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        while i < len(s):
            if s.count(s[i]) < 2:
                return(i)
            else:
                return(-1)
            i = i + 1