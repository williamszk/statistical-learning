/* Write a program that can make matrix sum, 
 * multiplication and inversion
 * */

#include <iostream>


void printMatrix(int matrix[2][2])
/* The objective of this function is to print a matrix in the
 * console.
 * For now I can only pass 2x2 dimensional matrices.
 * Later we'll try to do with any generic size of matrix.
 * */
{
    std::cout << "+          +" << std::endl;
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            if (j == 0) {
                std::cout << "|";
            }
            std::cout << "  " << matrix[i][j] << "  "; 
            
            if (j == 1)
            {
                std::cout << "|" << std::endl;
            }
        }
    }
    std::cout << "+          +" << std::endl << std::endl;
}


int** multiplyMatrixAndDouble(int[2][2] matrix, double num)
{
   printMatrix(matrix);

   return matrix;
}

int main()
{

    int matrix01[2][2] = {{1, 2}, {3, 4}};
    int matrix02[2][2] = {{2, 3}, {4, 5}};

    // printMatrix(matrix01);
    // printMatrix(matrix02);
    
    multiplyMatrixAndDouble(matrix01);

    return 0;
}














