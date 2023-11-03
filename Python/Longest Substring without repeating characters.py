class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length
        charSet = set()
        l = 0
        longest = 1

        for i in range(length):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            longest = max(longest, len(charSet))
        return longest







