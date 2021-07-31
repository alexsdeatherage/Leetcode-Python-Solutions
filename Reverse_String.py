class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Plan:
        Init two pointers called l and r to the beginning and end of s
        Iterate to the middle of the array, and swap the characters of s[l] and s[r]
        """

        half_length = len(s) // 2
        l = 0
        r = len(s) - 1

        for _ in range(half_length):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1