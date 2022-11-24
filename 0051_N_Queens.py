'''
Problem: https://leetcode.com/problems/n-queens/

Runtime: 187 ms
Memory: 14.5 MB
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        self.n = n
        self.place_queen([])

        return self.ans


    def place_queen(self, queens: List[List[str]]) -> None:
        row = len(queens)

        if row == self.n:
            board = self.build_board(queens)
            self.ans.append(board)
            return

        for col in range(self.n):
            new_queens = queens + [[row, col]]
            if self.check_attacks(new_queens):
                self.place_queen(new_queens)


    def check_attacks(self, queens: List[List[int]]) -> bool:
        # check top-L to bottom-R diagonals and top-R to bottom-L diagonals
        if len({q[0] - q[1] for q in queens}) != len(queens): return False
        if len({q[0] + q[1] for q in queens}) != len(queens): return False

        # check colums
        if len({q[1] for q in queens}) != len(queens): return False

        return True


    def build_board(self, queens: List[List[int]]) -> List[List[int]]:
        board = [
            ''.join(
                ['Q' if q[1] == i else '.' for i in range(self.n)]
            ) for q in queens
        ]

        return board
