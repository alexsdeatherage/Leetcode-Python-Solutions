class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        input: nums = [1,7,3,6,5,6]
        output: 3

        left_sum == right_sum
        """

        left_sum = total_sum = 0

        i = 0
        while i < len(nums):
            total_sum += nums[i]
            i += 1

        i = 0
        while i < len(nums):
            if total_sum - nums[i] == left_sum:
                return i
            else:
                left_sum += nums[i]
                total_sum -= nums[i]

            i += 1

        return -1