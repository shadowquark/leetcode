#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
void quicksort(int l, int r, int *obj)
{
	if (l >= r)	return;
	int i = l, j = r, x = obj[r];
	while (i < j)
	{
		while (i < j && obj[i] <= x)	++ i;
		obj[j] = obj[i];
		while (i < j && obj[j] > x)		-- j;
		obj[i] = obj[j];
	}
	obj[i] = x;
	quicksort(l, i - 1, obj);
	quicksort(i + 1, r, obj);
}
int threeSumClosest(int *nums, int numsSize, int target)
{
	quicksort(0, numsSize - 1, nums);
	int abs(int x) {return x > 0 ? x : -x;}
	int out = nums[0] + nums[1] + nums[2];
	for (int i = 0; i < numsSize - 2; ++ i)
	{
		int j = i + 1, k = numsSize - 1;
		while (j < k)
		{
			int temp = nums[i] + nums[j] + nums[k];
			if (abs(target - temp) < abs(target - out))	out = temp;
			if (temp == target)	return target;
			if (temp < target)	++ j;
			if (temp > target)	-- k;
		}
	}
	return out;
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

