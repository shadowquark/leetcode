#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
int threeSumClosest(int* nums, int numsSize, int target)
{
	return 0;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	int m, n, a[500];
	fscanf(fin, "%d%d", &n, &m);
	for (int i = 0; i < n; ++ i )
		fscanf(fin, "%d", a + i);
	int out = threeSumClosest(a, n, m);
	printf("%d\n", out);
	fprintf(fout, "%d\n", out); 
	return 0;
}

