/*
Program Name: Matrix Transpose

Example:
Input:
Enter no. of rows and columns: 3 3
Enter values:
1 2 3
4 5 6
7 8 9

Output:
Diagnol of the matrix:
1
5
9

*/

#include <stdio.h>
#include<stdlib.h>

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
    
    if(m != n)
    { printf("Diagnol Elements not found\n");
    exit(0);
	}
	else{

    printf("Diagnol Elements of the matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++)
        	if(i==j)
            printf("%d ", x[j][i]);
        printf("\n");
    }
}

    return 0;
}
