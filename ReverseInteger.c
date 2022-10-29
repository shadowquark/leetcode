#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
int reverse(int x)
{
    if (x == -2147483648)   return 0;
	bool flag = x < 0 ? 1 : 0;
    if (flag)   x = -x;
	char s[11];
	int pos = 0;
	while (x)
	{
		s[pos ++] = x % 10 + '0';
		x /= 10;
	}
	s[pos] = 0;
	int base = 1, begin = -1, out = 0;
	while (!s[++ begin]);
    int a[10] = {2, 1, 4, 7, 4, 8, 3, 6, 4, 7};
    if (pos - begin == 10)
        for (int i = 0; i < 10; ++ i)
        {
            if (s[i] - '0' > a[i])  return 0;
            if (s[i] - '0' < a[i])  break;
        }
	for (int i = pos - 1; i >= begin; -- i)
	{
		out += base * (s[i] - '0');
        if (pos == 10 && i == 0) break;
		base *= 10;
	}
    return flag ? -out : out;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	int n;
	fscanf(fin, "%d", &n);
	int out = reverse(n);
	printf("%d\n", out);
	fprintf(fout, "%d\n", out);
	return 0;
}

