class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=collections.defaultdict()
        for ch in magazine:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1
        for c in ransomNote:
            if (c not in d) or (d[c]==0):
                return False
            else:
                d[c]-=1
        return True
