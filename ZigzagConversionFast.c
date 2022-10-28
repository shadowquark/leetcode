#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
typedef struct charchain
{
	char key;
	struct charchain *next;
}node;
char *convert(char *s, int numRows)
{
	int pos = -1, m = 2 * numRows - 2;
	while (s[++ pos]);
	node *head[1001], *tail[1001];
	for (int i = 0; i < numRows; ++ i)
	{
		head[i] = malloc(sizeof(node));
		head[i]->next = 0;
		head[i]->key = 0;
		tail[i] = head[i];
	}
	for (int i = 0; i < pos; ++ i)
	{
		int temp =	m ? i % m : 0;
		if (temp >= numRows) temp = m - temp;
		tail[temp]->next = malloc(sizeof(node));
		tail[temp]->next->key = s[i];
		tail[temp]->next->next = 0;
		tail[temp] = tail[temp]->next;
	}
	char *out = (char *) malloc(sizeof(char) * (pos + 1));
	int r = 0;
	for (int i = 0; i < numRows; ++ i)
		while (head[i]->next)
		{
			out[r ++] = head[i]->next->key;
			head[i] = head[i]->next;
		}
	out[r] = 0;
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

