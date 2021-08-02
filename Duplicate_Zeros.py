class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        Plan:
        Iterate though arr using a while loop and a pointer l
        If arr[l] == 0, then insert 0 to arr[l + 1] and pop arr

        """

        l = 0
        length = len(arr)
        while l < length:
            if arr[l] == 0:
                arr.insert(l + 1, 0)
                arr.pop(-1)
                l += 1
            l += 1