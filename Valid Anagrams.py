class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return frozenset ( Counter(s).items()) == frozenset(Counter(t).items())
