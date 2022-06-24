// https://blog.devgenius.io/level-up-as-a-software-engineer-by-writing-a-chess-engine-1d0ffc7aebf9

#include <stdio.h>

typedef struct chesspiece {
    char name[20];
    int x;
    int y;
    char type[10];
    char color[10];
} ChessPiece;

/**
 * Moves a piece to the specified position
 * @arg name is the name of the piece according to 
*/
void movePiece(ChessPiece piece, int x, int y){
    piece.name;
    piece.x;
    piece.y;
}


int main()
{

    // build a represetation of a chess board
    // make a piece on the board and implement
    // the moves of a pawn

    ChessPiece pawnBlack1 = {
        .name = "pawnBlack1",
        .x = 0,
        .y = 6,
        .type = "Pawn",
        .color = "Black",
    };

    ChessPiece pawnBlack2 = {
        .name = "pawnBlack2",
        .x = 1,
        .y = 6,
        .type = "Pawn",
        .color = "Black",
    };

    // create function that verifies that no piece
    // is on the same position of the board




    // a chess board can be a 2-d matrix
    // it has 8 by 8 of size  

    // we can have typedef structs for the types of pieces
    // of chess, inside the struct we should have the position
    // and also the color of the piece
    
    // we need methods to check which are the allowed moves in the board

    // we could have some kind of graphical representation on the 
    // terminal of the pieces




    return 0;
}



