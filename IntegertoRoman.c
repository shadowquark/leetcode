#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
char *intToRoman(int num)
{
	char *s[30] = {"MMM", "MM", "M", "CM", "DCCC", "DCC", "DC", "D", "CD",
					"CCC",	"CC", "C", "XC", "LXXX", "LXX", "LX", "L", "XL",
					"XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V", "IV",
					"III", "II", "I"};
	int a[30] = {3000, 2000, 1000, 900, 800, 700, 600, 500, 400,
					300, 200, 100, 90, 80, 70, 60, 50, 40,
					30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
	char *out = (char *) malloc(sizeof(char) * 16);
	int pos = 0;
	for (int i = 0; i < 30; ++ i)
		if (a[i] <= num)
		{
			int temp = -1;
			while (s[i][++ temp]) out[pos ++] = s[i][temp];
			num -= a[i];
		}
    out[pos] = 0;
	return out;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	int n;
	fscanf(fin, "%d", &n);
	char *out = intToRoman(n);
	printf("%s\n", out);
//	fprintf(fout, "%s\n", out);
	return 0;
}

