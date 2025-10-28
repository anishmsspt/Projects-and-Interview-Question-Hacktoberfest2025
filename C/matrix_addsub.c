#include <stdio.h>
#define MAX 15

void readMatrix(int m, int n, int a[m][n]) {
    printf("Enter %dx%d elements:\n", m, n);
    int i, j;
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
            scanf("%d", &a[i][j]);
}

void printMatrix(int m, int n, int a[m][n]) {
    int i, j;
    for(i = 0; i < m; i++) {
        for(j = 0; j < n; j++)
            printf("%d ", a[i][j]);
        printf("\n");
    }
}

void addMatrix(int m, int n, int a[m][n], int b[m][n], int res[m][n]) {
    int i, j;
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
            res[i][j] = a[i][j] + b[i][j];
    printf("\nThe addition of matrices is:\n");
    printMatrix(m, n, res);
}

void subMatrix(int m, int n, int a[m][n], int b[m][n], int res[m][n]) {
    int i, j;
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
            res[i][j] = a[i][j] - b[i][j];
    printf("\nThe subtraction of matrices is:\n");
    printMatrix(m, n, res);
}

int main() {
    int m, n, p, q;
    int a[MAX][MAX], b[MAX][MAX], res[MAX][MAX];

    printf("Enter rows & cols of first matrix: ");
    scanf("%d %d", &m, &n);
    printf("Enter rows & cols of second matrix: ");
    scanf("%d %d", &p, &q);

    printf("\nFirst matrix:\n");
    readMatrix(m, n, a);
    printf("\nSecond matrix:\n");
    readMatrix(p, q, b);

    printf("\nFirst Matrix:\n");
    printMatrix(m, n, a);
    printf("\nSecond Matrix:\n");
    printMatrix(p, q, b);

    if (m == p && n == q) {
        addMatrix(m, n, a, b, res);
        subMatrix(m, n, a, b, res);
    } else {
        printf("\nMatrix addition/subtraction not possible (order mismatch).\n");
    }

    return 0;
}