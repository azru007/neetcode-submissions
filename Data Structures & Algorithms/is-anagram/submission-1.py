class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc= Counter(s)
        tc= Counter(t)
        if tc==sc:
            return True
        else: return False