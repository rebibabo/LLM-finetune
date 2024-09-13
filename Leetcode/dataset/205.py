class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        for m, n in zip(s, t):
            if n not in map1:
                map1[n] = m
            else:
                if m != map1[n]:
                    return False
            if m not in map2:
                map2[m] = n
            else:
                if n != map2[m]:
                    return False 
        return True