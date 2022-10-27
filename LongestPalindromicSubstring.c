#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

char *output(const char *x, int tot)
{
    int pos = 0;
    char *y = (char*) malloc(sizeof(char*) * (tot + 1));
    for (int i = 1; i < 2 * tot; ++ i)
        if (x[i] != '\n')   y[pos ++] = x[i];
    y[tot] = '\0';
    return y;
}

char *longestPalindrome(char *s){
    int pos = 0, maxP = 0, maxR = 0, global_max = 0, maxlen[2002];
    char ss[2002], *out;
    memset(ss, 0, sizeof(ss));
    memset(maxlen, 0, sizeof(maxlen));
    ss[0] = '\n';
    while (s[pos]) 
    {
        ss[2 * (pos ++) + 1] = s[pos];
        ss[2 * pos] = '\n';
    }
    pos = 2 * pos + 1;
    for (int i = 1; i < pos; ++ i)
    {
        if (i + global_max > pos - 2)    break;
        int r = 0;
        if (i - maxP > maxR)    
        {
            maxR = 0;
            maxP = i;
        }
        if (maxR && maxlen[2 * maxP - i] != maxP + maxR - i)
            continue;
        else
            r = maxP + maxR - i;
        while (i - r >= 0 && i + r < pos && ss[i + r] == ss[i - r])
            r ++;
        maxlen[i] = -- r;
        if (r > maxR)
        {
            maxR = r;
            maxP = i;
        }
        if (r > global_max)
        {
            global_max = r;
            out = ss + i - r;
        }
    }
    return output(out, global_max);
}

int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	char s[1001];
	fscanf(fin, "%s", s);
	fprintf(fout, "%s", longestPalindrome(s));
	return 0;
}

