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

void uppTriangle(int m, int n, int a[m][n]) {
    int i, j;
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
          if(i<j || i==j)
            printf("%d ", a[i][j]);
}

void lowTriangle(int m, int n, int a[m][n]) {
    int i, j;
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
          if(i>j || i==j)
            printf("%d ", a[i][j]);
}

int main() {
    int m, n;
    int a[MAX][MAX];

    printf("Enter rows & cols of first matrix: ");
    scanf("%d %d", &m, &n);

    printf("\nInput matrix:\n");
    readMatrix(m, n, a);
    printf("\nGiven Matrix:\n");
    printMatrix(m, n, a);
    
    printf("\nUpper triangular elements of Matrix:\n");
    uppTriangle(m,n,a);

    printf("\nLower triangular elements of the Matrix:\n");
    lowTriangle(m,n,a);
   

    return 0;
}