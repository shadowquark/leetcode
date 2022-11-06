#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<stdbool.h>
char **letterCombinations(char *digits, int *returnSize)
{
	char **x = {"abc", "def"};
	return x;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	char *s;
	int *n;
	fscanf(fin, "%s", s);
	char **out = letterCombinations(s, n);
	for (int i = 0; i < *n; ++ i)
	{
		printf("%s, ", out[i]);
		fprintf(fout, "%s, ", out[i]);
	}
	return 0;
}

