#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
char *convert(char *s, int numRows)
{
	int a[1001], pos = -1, m = 2 * numRows - 2;
	memset(a, 0, sizeof(a));
	while (s[++ pos]);
	for (int i = 0; i < pos; ++ i)
	{
		a[i] = m ? i % m : 0;
		if (a[i] >= numRows) a[i] = m - a[i];
	}
	char *out = (char *) malloc(sizeof(char) * (pos + 1));
	int tail = 0;
	for (int i = 0; i < numRows; ++ i)
		for (int j = 0; j < pos; ++ j)
			if (a[j] == i)	out[tail ++] = s[j];
	out[tail] = 0;
	return out;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	char s[1001];
	int n;
	fscanf(fin, "%s%d", s, &n);
	printf("%s", convert(s, n));
	fprintf(fout, "%s", convert(s, n));
	return 0;
}

