class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        l = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1

            if (r - l + 1 - max(count.values())) <= k:
                result = max(result, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return result







