class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        jewel_stones = set()

        for index in range(0, len(jewels)):
            jewel_stones.add(jewels[index])

        for j in range(0, len(stones)):
            if stones[j] in jewel_stones:
                counter += 1

        return counter
