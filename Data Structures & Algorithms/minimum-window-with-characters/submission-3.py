class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        contset = set()
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
            contset.add(c)
        minlen = float("inf")
        minl = 0
        minr = 0
        l = 0
        for r in range(len(s)):
            if s[r] in t_map:
                t_map[s[r]] -= 1
                if t_map[s[r]] == 0:
                    contset.remove(s[r])
                while not contset:
                    if r - l + 1 < minlen:
                        minlen = r - l + 1
                        minl = l
                        minr = r
                    if s[l] in t_map:
                        t_map[s[l]] += 1
                        if t_map[s[l]] == 1:
                            contset.add(s[l])
                    l += 1
        
        if minlen == float("inf"):
            return ""
        else:
            return s[minl:minr+1]



                

        