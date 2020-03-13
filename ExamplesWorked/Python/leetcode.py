class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        if s == "" or s[0] == s[1]:
            j = -1
            return j
        j = 0
        s.upper()
        for i in s:
            i.upper()
            s = s[1:]
            x = i in s
            if x == False:
                print(i, "is Not Unique")
                return j
            else:
                j = j + 1
        