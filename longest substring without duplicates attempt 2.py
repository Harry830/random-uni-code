def lengthoflongestSubstring(s):
        currWindowSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in currWindowSet:
                currWindowSet.add(s[r])
                res = max(res,(r-l+1))
            else:
                while s[r] in currWindowSet:
                    currWindowSet.remove(s[l])
                    l +=1
                currWindowSet.add(s[r])
        return res

print(lengthoflongestSubstring("abcabcbb"))


