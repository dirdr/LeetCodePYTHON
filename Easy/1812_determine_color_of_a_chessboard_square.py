class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ord(coordinates[0]) % 2 != int(coordinates[1]) % 2
        
# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Determine Color of a Chessboard Square.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Determine Color of a Chessboard Square.
        
