# 2352. Equal Row and Column Pairs
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        for i in grid:
            row = tuple(i)
            row_count[row] += 1
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            col_count[col] += 1
        count = 0
        for key in row_count:
            if key in col_count:
                count += row_count[key] * col_count[key]
        return count
