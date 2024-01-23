"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = list(haystack)
        changed = False
        for i in range(len(haystack)-len(needle)+1):
            check = True
            for j in range(len(needle)):
                if s[i+j] != needle[j]:
                    check=False
                    break
            if check:
                changed = True
                for j in range(len(needle)):
                    return i+j
        return -1
if __name__ == "__main__":
    obj = Solution()
    show = obj.strStr("sadbutsad","sad")
    print(show)
