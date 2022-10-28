#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
int lengthOfLongestSubstring(char *s)
{
    int head, tail, length, maxlength;
    head = tail = length = maxlength = 0;
    bool a[256];
    memset(a, 0, sizeof(a));
    for (; s[tail] != '\0'; ++ tail)
    {
        int num = (int)s[tail];
        if (a[num])
        {
            if (length > maxlength) maxlength = length;
            while (s[head ++] - s[tail])
            {
                a[(int)s[head - 1]] = 0;
                -- length;
            }
        } else {
            a[num] = 1;
            length ++;
        }
    }
    if (length > maxlength) maxlength = length;
    return maxlength;
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	char s[256];
	fscanf(fin, "%s", s);
	fprintf(fout, "%d\n", lengthOfLongestSubstring(s));
	return 0;
}

