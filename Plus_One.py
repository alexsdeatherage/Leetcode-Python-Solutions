class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0

        if digits[-1] == 10:
            carry = 1

        index = -1

        while len(digits) > abs(index) and carry == 1:
            digits[index - 1] += 1
            digits[index] = 0
            carry = 0
            if digits[index - 1] == 10:
                carry = 1
            index -= 1

        if carry == 1:
            digits.insert(0, 1)
            digits[1] = 0

        return digits
