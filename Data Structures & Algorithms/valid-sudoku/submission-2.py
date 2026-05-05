import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                square_id = (r //3, c // 3)
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[square_id]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[square_id].add(val)
        return True
