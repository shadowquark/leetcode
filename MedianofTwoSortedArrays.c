#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
int findPos(int *a, int length, int num)
{
	if (a[0] > num)	return 0;
	int pos = length / 2, begin = 0, end = length;
	for (;;)
	{
		if (a[pos] <= num && (pos == length - 1 || a[pos + 1] > num))
			return pos + 1;
		if (a[pos] <= num)
		{
			begin = pos;
			pos = (pos + end) / 2;
		}
		if (a[pos] > num)	
		{
			end = pos;
			pos = (begin + pos) / 2;
		}
	}
}
double findMedianSortedArrays(
	int *nums1, int nums1Size, int *nums2, int nums2Size
){
	bool flag = 0;
	int medianPos = (nums1Size + nums2Size) / 2 + 1;
	if (!((nums1Size + nums2Size) & 1))
	{
		flag = 1;
		-- medianPos;
	}
	if (!nums1Size)
		return (nums2[medianPos - 1] + nums2[medianPos - 1 + flag]) / 2.;
	if (!nums2Size)
		return (nums1[medianPos - 1] + nums1[medianPos - 1 + flag]) / 2.;
	int begin1 = 0, begin2 = 0, length1 = nums1Size, length2 = nums2Size;
	while (medianPos > 0)
	{
		int smaller = findPos(nums1 + begin1, length1, nums2[begin2]);
		if (medianPos <= smaller)
		{
			if (!flag)	return nums1[begin1 + medianPos - 1];
			if (medianPos - smaller)
				return (nums1[begin1 + medianPos - 1] 
						+ nums1[begin1 + medianPos]) / 2.;
			return (nums1[begin1 + smaller - 1] + nums2[begin2]) / 2.;
		}
		length1 -= smaller;
		medianPos -= smaller;
		if (!length1)
			return (nums2[begin2 + medianPos - 1]
					+ nums2[begin2 + medianPos - 1 + flag]) / 2.;
		begin1 += smaller;
		smaller = findPos(nums2 + begin2, length2, nums1[begin1]);
		if (medianPos <= smaller)
		{
			if (!flag)	return nums2[begin2 + medianPos - 1];
			if (medianPos - smaller)
				return (nums2[begin2 + medianPos - 1] 
						+ nums2[begin2 + medianPos]) / 2.;
			return (nums2[begin2 + smaller - 1] + nums1[begin1]) / 2.;
		}
		length2 -= smaller;
		medianPos -= smaller;
		if (!length2)
			return (nums1[begin1 + medianPos - 1]
					+ nums1[begin1 + medianPos - 1 + flag]) / 2.;
		begin2 += smaller;
//		printf("smaller: %d, medianPos: %d, begin: %d, length: %d\n", 
//				smaller, medianPos, begin2, length2);
	}
	return 0;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	int num1, nums1[1000], num2, nums2[1000];
	fscanf(fin, "%d", &num1);
	for (int i = 0; i < num1; ++ i)
		fscanf(fin , "%d", nums1 + i);
	fscanf(fin, "%d", &num2);
	for (int i = 0; i < num2; ++ i)
		fscanf(fin , "%d", nums2 + i);
//	printf("%lf\n", findMedianSortedArrays(nums1, num1, nums2, num2));
	fprintf(fout, "%lf\n", findMedianSortedArrays(nums1, num1, nums2, num2));
	return 0;
}

