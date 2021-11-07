data class SudokuPuzzle(
    val boundary: Int,
    val difficulty: Difficulty,
    val graph: LikedHashMap<Int, LinkedList<SudokuNode>>
    = buildNewSudoku(boundary, difficulty).graph,
    var elapsedTime: Long = 0L
): Serializable {
    fun getValue(): LinkedHashMap<Int, <LinkedList<SudokuNode>> = graph
}