package com.bracketcove.graphsudoku.domain

enum class Difficulty(val modifier: Double) {
    EASY(0.5),
    MEDIUM(0.44),
    HARD(0.38)
}



// kotlinc Difficulty.kt -include-runtime -d Difficulty.jar
// java -jar Difficulty.jar