#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<stdbool.h>
int obScheduling(int *startTime, int startTimeSize,
					int *endTime, int endTimeSize,
					int *profit, int profitSize)
{
	int n = profitSize, ;
	
	return 0;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	int n, a[50000], b[50000], c[50000];
	fscanf(fin, "%d", &n);
	for (int i = 0; i < n; ++ i)
		fscanf(fin, "%d%d%d", a, b, c);
	int out = obScheduling(a, n, b, n, c, n);
	printf("%d\n", out);
	fprintf(fout, "%d\n", out);
	return 0;
}

