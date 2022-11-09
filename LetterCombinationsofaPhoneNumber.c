#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<stdbool.h>
char **letterCombinations(char *digits, int *returnSize)
//void letterCombinations(char *digits, int *returnSize)
{
	int lens = strlen(digits);
	returnSize = malloc(sizeof(int));
	*returnSize = 0;
	int a[8] = {3, 3, 3, 3, 3, 4, 3, 4}, pos = 0;
	char *phone[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
	char **out = malloc(sizeof(char));
	for (int i = 0; i < lens; ++ i)
	{
		int key = *(digits + i) - '2';
		*returnSize += a[key];
		for (int j = 0; j < strlen(phone[i]); ++ j)
		{
			*(out + j) = malloc(sizeof(char) * i);
			*(*(out + j) + i) = *(phone[i] + j);
		}
		printf("%s, ", *out + i);
		printf("%s\n", *(out + 1) + i);
	}
	printf("%d\n", *returnSize);
	*out = "abc";
	*(out + 8) = "bcd";
	printf("%s\n", *(out + 8));
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	char *s;
	int *n;
	fscanf(fin, "%s", s);
	letterCombinations(s, n);
//	char **out = letterCombinations(s, n);
//	for (int i = 0; i < *n; ++ i)
//	{
//		printf("%s, ", out[i]);
//		fprintf(fout, "%s, ", out[i]);
//	}
	return 0;
}

