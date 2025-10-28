/*
Program Name: Matrix Transpose

Example:
Input:
Enter no. of rows and columns: 2 3
Enter values:
1 2 3
4 5 6

Output:
Transpose of the matrix:
1 4
2 5
3 6

*/

#include <stdio.h>

int main() {
    int i, j, m, n;

    printf("Enter number of rows and columns: ");
    scanf("%d%d", &m, &n);

    int x[m][n];
    printf("Enter values:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &x[i][j]);
        }
    }
    
    printf("Given matrix:\n");
    for(i=0;i<m;i++)
    {
	for(j=0;j<n;j++)
	printf("%d",x[i][j]);
	printf("\n");
    }
    printf("Transpose of the matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            printf("%d ", x[j][i]);
        }
        printf("\n");
    }

    return 0;
}