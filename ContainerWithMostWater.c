#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
int maxArea(int* height, int heightSize)
{
	int l = 0, r = heightSize - 1, max = 0;
	while (l < r)
	{
		int temp = height[l] - height[r];
		if (max < (r - l) * (temp < 0 ? height[l] : height[r]))
			max = (r - l) * (temp < 0 ? height[l] : height[r]);
		if (temp < 0)
			++ l;
		else
			-- r;
	}
	return max;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	int n, a[100001];
	fscanf(fin, "%d", &n);
	for (int i = 0; i < n; ++ i)
		fscanf(fin, "%d", a + i);
	int out = maxArea(a, n);
	printf("%d\n", out);
	fprintf(fout, "%d\n", out);
	return 0;
}

