from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sCtr = Counter(s)
        tCtr = Counter(t)

        for letter, count in sCtr.items():
            if count != tCtr[letter]:
                return False

        return True