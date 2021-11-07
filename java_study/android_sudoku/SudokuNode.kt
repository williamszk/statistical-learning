package com.bracketcove.graphsudoku.domain

data class SudokuNode(
    val x: Int,
    val y: Int,
    var color: Int = 0,
    var readOnly: Boolean = true
): Serializable {
    override fun hashCode(): Int {
        return getHash(x, y)
    }
}

internal fun getHash(x: Int, y: Int): Int {
    val newX = x*100
    return "$newX$y".toInt()
}
