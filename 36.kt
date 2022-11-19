class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        val square = arrayOf(
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.')
        )
        val col = arrayOf(
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.'),
            charArrayOf('.','.','.','.','.','.','.','.','.')
        )
        for (i in board.indices) {
            for (j in board[i].indices) {
                square[i][j] = board[(i/3*3) + (j/3)][3*(i%3) + (j%3)]
                col[i][j] = board[j][i]
            }
        }
        for (row in board) {
            val filtered = row.filter { it != '.' }
            if (filtered.size != filtered.distinct().size) {
                return false
            }
        }
        for (row in square) {
            val filtered = row.filter { it != '.' }
            if (filtered.size != filtered.distinct().size) {
                return false
            }
        }
        for (row in col) {
            val filtered = row.filter { it != '.' }
            if (filtered.size != filtered.distinct().size) {
                return false
            }
        }
        return true
    }
}