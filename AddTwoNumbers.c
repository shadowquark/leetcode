#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
struct ListNode
{
    int val;
    struct ListNode *next;
};

void output(struct ListNode* l, char split, FILE *fout)
{
	struct ListNode *tail = l;
	while (tail)
	{
		if (tail->next)
			fprintf(fout, "%d%c", tail->val, split);
		else
			fprintf(fout, "%d", tail->val);
		tail = tail->next;
	}
	fputc('\n', fout);
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
	int base = 0;
    	bool next1 = 1, next2 = 1;
    	struct ListNode *head = malloc(sizeof(struct ListNode)), *tail = head;
    	do 
    	{
			int num1 = 0, num2 = 0;
			if (l1) num1 = l1->val;
			if (l2) num2 = l2->val;
			if (l1 && !l1->next)    next1 = 0;
			if (l2 && !l2->next)    next2 = 0;
			if (num1 + num2 + base < 10)
			{
				tail->val = num1 + num2 + base;
				base = 0;
			} else {
				tail->val = num1 + num2 + base - 10;
				base = 1;
			}
			if (next1 || next2)
			{
				tail->next = malloc(sizeof(struct ListNode));
				tail = tail->next;
			}
			if (l1)	l1 = l1->next;
			if (l2) l2 = l2->next;
			if (!next1 && !next2)	tail->next = 0;
    	} while (l1 || l2);
    	if (base)
    	{
			tail->next = malloc(sizeof(struct ListNode));
			tail->next->next = 0;
			tail->next->val = 1;
    	}
    	return head;
}

int main()
{
	FILE *fin = fopen("oo.xx", "r");
	FILE *fout = fopen("xx.oo", "w");
	struct ListNode *l1, *l2, *tail, *previous;
	l1 = malloc(sizeof(struct ListNode));
	l2 = malloc(sizeof(struct ListNode));
	tail = l1;
	char temp;
	bool flag = 0;
	while (fscanf(fin, "%c", &temp) != EOF)
	{
		if (temp == ' ' || temp == ',')	continue;
		if (temp == '\n')
		{
			free(tail);
			previous->next = 0;
			if (flag)	break;
			tail = l2;
			flag = 1;
			continue;
		}
		tail->val = temp - '0';
		tail->next = malloc(sizeof(struct ListNode));
		previous = tail;
		tail = tail->next;
	}
	output(addTwoNumbers(l1, l2), ',', fout);
	return 0;
}

