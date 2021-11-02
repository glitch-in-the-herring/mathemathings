#include <stdio.h>

int main(void)
{
    int y1, x1;
    printf("Enter the dimensions of A (col row): ");
    scanf("%d %d", &y1, &x1);
    int y2, x2;
    printf("Enter the dimensions of B (col row): ");
    scanf("%d %d", &y2, &x2);

    if (x1 != y2)
    {
        printf("Matrices cannot be multiplied!");
        return 0;
    }

    long long int A[y1][x1];
    long long int B[y2][x2];

    printf("Enter the contents of A:\n");

    for (int i = 0; i < y1; i++)
    {
        for (int j = 0; j < x1; j++)
        {
            scanf("%lld", &A[i][j]);
        }
    }

    printf("Enter the contents of B:\n");
    for (int i = 0; i < y2; i++)
    {
        for (int j = 0; j < x2; j++)
        {
            scanf("%lld", &B[i][j]);
        }
    }

    printf("Product of A*B:\n");
    long long int cell;
    for (int i = 0; i < y1; i++)
    {
        for (int j = 0; j < x2; j++)
        {
            cell = 0;
            for (int k = 0; k < x1; k++)
            {
                cell += A[i][k] * B[k][j];
            }
            printf("%-8lld", cell);
        }
        printf("\n");
    }
}
