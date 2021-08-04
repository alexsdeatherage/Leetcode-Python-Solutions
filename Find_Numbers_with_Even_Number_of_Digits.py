class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Don't have to worry about empty lists

        Plan:
        1. Iterate through nums using a for loop
        2. For each iteration, find the number of digits for integer
        3. If digits is even, add to counter
        4. Return counter
        """

        counter = 0
        for i in nums:
            digits = 0
            while i > 0:
                digits += 1
                i = i // 10
            if digits % 2 == 0:
                counter += 1

        return counter
