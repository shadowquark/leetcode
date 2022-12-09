#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<stdbool.h>
void quicksort(int l, int r, int *a, int *b, int *c)
{
	if (l >= r)	return;
	int i = l, j = r, x[3] = {a[r], b[r], c[r]};
	while (i < j)
	{
		while (i < j && b[i] <= x[1])	++ i;
		a[j] = a[i];
		b[j] = b[i];
		c[j] = c[i];
		while (i < j && b[j] > x[1])	-- j;
		a[i] = a[j];
		b[i] = b[j];
		c[i] = c[j];
	}
	a[i] = x[0];
	b[i] = x[1];
	c[i] = x[2];
	quicksort(l, i - 1, a, b, c);
	quicksort(i + 1, r, a, b, c);
}
int findlast(int y, int *x, int n)
{
	if (y >= x[n])	return n;
	int l = 0, r = n;
	while (l < r)
	{
		if (y < x[(l + r) / 2])
			r = (l + r) / 2;
		else
			l = (l + r) / 2 + 1;
	}
	return l - 1;
}
int jobScheduling(int *startTime, int startTimeSize,
					int *endTime, int endTimeSize,
					int *profit, int profitSize)
{
	int n = profitSize;
	quicksort(0, n - 1, startTime, endTime, profit);
	int a[50001], b[50001];
	a[0] = b[0] = 0;
	for (int i = 0; i < n; ++ i)
	{
		printf("%d\n", i);
		int pos = findlast(*(startTime + i), b, i);
		if (a[pos] + *(profit + i) > a[i])
		{
			a[i + 1] = a[pos] + *(profit + i);
			b[i + 1] = *(endTime + i);
		}
		else
		{
			a[i + 1] = a[i];
			b[i + 1] = b[i];
		}
	}
	return a[n];
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	int n, a[50000], b[50000], c[50000];
	fscanf(fin, "%d", &n);
	for (int i = 0; i < n; ++ i)
		fscanf(fin, "%d,", a + i);
	for (int i = 0; i < n; ++ i)
		fscanf(fin, "%d,", b + i);
	for (int i = 0; i < n; ++ i)
		fscanf(fin, "%d,", c + i);
	int out = obScheduling(a, n, b, n, c, n);
	printf("%d\n", out);
	fprintf(fout, "%d\n", out);
	return 0;
}

