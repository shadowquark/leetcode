#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
bool match(char *s1, int len1, char *s2, int len2, char previous)
{
	if (!len1)
	{
		for (int i = 0; i < len2; ++ i)
			if (s2[i] != '*' && s2[i + 1] != '*')	return 0;
		return 1;
	}
	if (s1[0] == s2[0] || s2[0] == '.')
		if (s2[1] == '*')
			return match(s1 + 1, len1 - 1, s2 + 1, len2 - 1, s2[0])\
					|| match(s1, len1, s2 + 1, len2 - 1, 0);
		else
			return match(s1 + 1, len1 - 1, s2 + 1, len2 - 1, 0);
	if (s2[1] == '*')	return match(s1, len1, s2 + 1, len2 - 1, s2[0]);
	if (s2[0] != '*')	return 0;
	if (previous == '.' || previous == s1[0])
		return match(s1 + 1, len1 - 1, s2, len2, previous)\
					|| match(s1, len1, s2 + 1, len2 - 1, 0);
	else
		return match(s1, len1, s2 + 1, len2 - 1, 0); 
}
// Leetcode Version
//bool isMatch(char *s, char *p)
//{
//	int len1 = -1, len2 = -1;
//	while (s[++ len1]);
//	while (p[++ len2]);
//	char s1[21], s2[31];
//	for (int i = 0; i < len1; ++ i)
//		s1[i] = s[i];
//	for (int i = 0; i < len2; ++ i)
//		s2[i] = p[i];
//	s1[len1] = s2[len2] = 0;
//
//	bool f[21][31];
//	memset(f, 0, sizeof(f));
//	f[len1][len2] = 1;
//	for (int j = len2 - 1; j > 0; -- j)
//		if (s2[j] == '*' && f[len1][j + 1])
//			f[len1][j] = f[len1][j - 1] = 1;
//	for (int i = len1 - 1; i >= 0; -- i)
//		for (int j = len2 - 1; j >= 0; --j)
//		{
//			if (s2[j + 1] == '*')
//				f[i][j] = f[i][j + 2];
//			if (s2[j] == '.' || s2[j] == s1[i])
//				if (s2[j + 1] == '*')
//					f[i][j] = (s1[i] == s1[i + 1] || s2[j] == '.')
//								&& f[i + 1][j] || f[i + 1][j + 2] || f[i][j];
//				else
//					f[i][j] = f[i + 1][j + 1];
//		}
//	return f[0][0];
////	return match(s1, len1, s2, len2, 0);
//}
// Local Version
bool isMatch(char *s1, char *s2)
{
	int len1 = -1, len2 = -1;
	while (s1[++ len1]);
	while (s2[++ len2]);

	bool f[21][31];
	memset(f, 0, sizeof(f));
	f[len1][len2] = 1;
	for (int j = len2 - 1; j > 0; -- j)
		if (s2[j] == '*' && f[len1][j + 1])
			f[len1][j] = f[len1][j - 1] = 1;
	for (int i = len1 - 1; i >= 0; -- i)
		for (int j = len2 - 1; j >= 0; --j)
		{
			if (s2[j + 1] == '*')
				f[i][j] = f[i][j + 2];
			if (s2[j] == '.' || s2[j] == s1[i])
				if (s2[j + 1] == '*')
					f[i][j] = (s1[i] == s1[i + 1] || s2[j] == '.')
								&& f[i + 1][j] || f[i + 1][j + 2] || f[i][j];
				else
					f[i][j] = f[i + 1][j + 1];
		}
	return f[0][0];
//	return match(s1, len1, s2, len2, 0);
}
int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	char s1[21], s2[31];
	fscanf(fin, "%s%s", s1, s2);
//	printf("%s\n%s\n", s1, s2);
	char *out = isMatch(s1, s2) ? "true" : "false";
	printf("%s\n", out);
	fprintf(fout, "%s\n", out);
	return 0;
}

