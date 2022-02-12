class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = collections.Counter( ransomNote )
        count2 = collections.Counter( magazine )
        count.subtract(count2)
        for key in count:
            if count[key] > 0:
                return False
        return True
