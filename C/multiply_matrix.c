#include <stdio.h>

// Function to get matrix elements entered by the user
void getMatrixElements(int matrix[][10], int row, int column) {
    printf("\nEnter elements: \n");
    int i, j;
    for (i = 0; i < row; ++i) {
        for (j = 0; j < column; ++j) {
            printf("Enter a%d%d: ", i + 1, j + 1);
            scanf("%d", &matrix[i][j]);
        }
    }
}

// Function to multiply two matrices
void multiplyMatrices(int first[][10],
                      int second[][10],
                      int result[][10],
                      int r1, int c1, int r2, int c2) {
    int i, j, k;

    // Initialize result matrix elements to 0
    for (i = 0; i < r1; ++i)
        for (j = 0; j < c2; ++j)
            result[i][j] = 0;

    // Matrix multiplication logic
    for (i = 0; i < r1; ++i) {
        for (j = 0; j < c2; ++j) {
            for (k = 0; k < c1; ++k) {
                result[i][j] += first[i][k] * second[k][j];
            }
        }
    }
}

// Function to display the matrix
void display(int result[][10], int row, int column) {
    int i, j;
    printf("\nOutput Matrix:\n");
    for (i = 0; i < row; ++i) {
        for (j = 0; j < column; ++j) {
            printf("%d  ", result[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int first[10][10], second[10][10], result[10][10];
    int r1, c1, r2, c2;

    printf("Enter rows and columns for the first matrix: ");
    scanf("%d %d", &r1, &c1);
    printf("Enter rows and columns for the second matrix: ");
    scanf("%d %d", &r2, &c2);

    // Check for valid matrix multiplication condition
    while (c1 != r2) {
        printf("Error! Column of first matrix not equal to row of second.\n");
        printf("Enter rows and columns for the first matrix: ");
        scanf("%d %d", &r1, &c1);
        printf("Enter rows and columns for the second matrix: ");
        scanf("%d %d", &r2, &c2);
    }

    // Input matrices
    printf("\nEnter first matrix:\n");
    getMatrixElements(first, r1, c1);

    printf("\nEnter second matrix:\n");
    getMatrixElements(second, r2, c2);

    // Multiply two matrices
    multiplyMatrices(first, second, result, r1, c1, r2, c2);

    // Display result
    display(result, r1, c2);

    return 0;
}