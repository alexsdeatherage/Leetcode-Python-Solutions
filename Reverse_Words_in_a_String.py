class Solution:
    def reverseWords(self, s: str) -> str:
        """
        1. Init array
        2. Append each word to the array
        3. Reverse each indiviual work in the array
        4. Use join method and return array
        """

        # Splits string into array by whitespace
        arr = s.split()
        new_arr = list()
        # Reverses each word in array
        for word in arr:
            new_arr.append(word[::-1])

        # Joins string elements of array into one string
        return ' '.join(new_arr)