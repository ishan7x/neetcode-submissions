class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l = res = maxA = 0
        for r in s:
            if r not in myset:
                myset.add(r)
                res += 1
            else:
                # we have seen this before
                while r in myset:
                    myset.remove(s[l])
                    l+=1
                    res-=1
                myset.add(r)
                res+=1
            maxA = max(maxA, res)
        return maxA
            
                
        