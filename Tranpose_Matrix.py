class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Plan:

        Note, needed a bit of help online for this solution. Yes, I know.

        """
        # Get the column and row for the given matrix
        column, row = len(matrix), len(matrix[0])

        # Init empty matrix of same width and height
        new_matrix = [[0 for x in range(column)] for y in range(row)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[j][i] = matrix[i][j]

        return new_matrix
