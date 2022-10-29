#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
int myAtoi(char *s)
{
	int begin = -1;
	bool flag = 0;
	while (s[++ begin] == ' ');
	if (s[begin] == '-' || s[begin] == '+')
	{
		flag = s[begin] == '+' ? 0 : 1;
		++ begin;
	}
	if (s[begin] < '0' || s[begin] > '9')	return 0;
	while (s[begin ++] == '0');
	if (s[-- begin] < '0' || s[begin] > '9')	return 0;
	int end = begin;
	while (s[++ end] >= '0' && s[end] <= '9');
	int out = 0, base = 1, check = end - begin;
	if (check > 10)	return flag ? -2147483648 : 2147483647;
	int a[10] = {2, 1, 4, 7, 4, 8, 3, 6, 4, 7};
	if (flag)	a[9] = 8;
	if (check == 10)
		for (int i = begin; i < end; ++ i)
		{
			if (s[i] - '0' > a[i - begin])
				return flag ? -2147483648 : 2147483647;
			if (s[i] - '0' < a[i - begin])	break;
            if (i == end - 1 && s[i] - '0' == a[9]) 
				return flag ? -2147483648 : 2147483647;
		}
	for (int i = end - 1; i >= begin; -- i)
	{
		out += base * (s[i] - '0');
		if (!-- check)	break;
		base *= 10;
	}
	return flag ? -out : out;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	char s[201];
	fscanf(fin, "%s", s);
	int out = myAtoi(s);
	printf("%d\n", out);
	fprintf(fout, "%d\n", out);
	return 0;
}

