class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = []
        for i in s:
            if i in a:
                pass
            else:
                if s.count(i)==1:
                    return s.index(i)
                else:
                    a.append(i)
        return -1
