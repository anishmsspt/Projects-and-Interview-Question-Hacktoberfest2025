#include<stdio.h>
#include <stdlib.h>
int main(){

int rows,cols,i=0,j=0,matr[10][10];
printf("Enter the Number of rows:");
scanf("%d",&rows);
if(rows==0 || rows>10)
{
	printf("Invalid Row Input");
	exit(0);
}
printf("Enter the Number of Columns:");
scanf("%d",&cols);
if(cols==0 || cols>10)
{
	printf("Invalid Column Input");
	exit(0);

}
for(i=0;i<rows;i++)
{
	printf("Enter %d row elements:\n",(i+1));
	for(j=0;j<cols;j++)
	{
		scanf("%d",&matr[i][j]);
	}
}
printf("The matrix entered is-\n");
for(i=0;i<rows;i++)
{
	for(j=0;j<cols;j++)
	{
		printf("%d",matr[i][j]);
	}
	printf("\n");
}
}