def max_char_window(s):
    dict1 = {}
    for char in s:
        dict1[char] = 0
    for char in s:
        dict1[char] += 1

    return dict1[max(dict1, key=dict1.get)]


def characterReplacement(s,k):
        res = 0

        l = 0

        for r in range(len(s)):
            if (r-l+1) - max_char_window(s[l:r+1]) > k :
                res = max(res,r-l)
                while (r-l+1) - max_char_window(s[r:l+1]) <= k:
                    l +=1

                
            else:
                res = max(res, r-l+1)
        return res


print(characterReplacement("AAABABB",1))

    
