class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l =0
        r=0
        maxlen=0
        d={}

        while r < len(s):
            if s[r] in d and d[s[r]]>=l:
                l = d[s[r]]+1
            maxlen = max(maxlen,r-l+1)
            d[s[r]] = r
            r+=1
        return maxlen
        