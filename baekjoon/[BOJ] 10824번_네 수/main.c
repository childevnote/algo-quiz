//[BOJ] 10824��_�� ��

#include <stdio.h>
#include <string.h> 
#include <stdlib.h>
#define MAX 1000000
#define MIN 1
int main()
{
	char cha[MAX + 1];
	char chb[MAX + 1];
	char chc[MAX + 1];
	char chd[MAX + 1];

	int a,b,c,d;

	scanf("%d %d %d %d", &a, &b, &c, &d);
	
	if (a < MIN || a >MAX || b < MIN || b >MAX || c < MIN || c >MAX || d < MIN || d >MAX) {
		printf("�ڿ��� ���� ���\n");
		exit(1);
	}

	sprintf(cha, "%d", a);
	sprintf(chb, "%d", b);
	sprintf(chc, "%d", c);
	sprintf(chd, "%d", d);

	strcat(cha, chb);
	strcat(chc, chd);
	
	long long A = atoi(cha);
	long long B = atoi(chc);

	printf("%lld\n", atoll(cha) + atoll(chc));

	return 0;
}