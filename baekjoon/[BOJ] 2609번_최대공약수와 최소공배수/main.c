//[BOJ] 2609��_�ִ������� �ּҰ����
#include <stdio.h>

int main()
{
	int a, b;
	int i, N = 0;
	int tmp = 0;

	scanf("%d %d", &a, &b);

	if (0 > a || a > 10000 || 0 > b || b > 10000) {
		printf("�ڿ����� ������ ������ϴ�.\n");
		return;
	}

	N = (a > b) ? b : a;
	for (i = 1; i <= N; i++)
	{
		if (a % i == 0 && b % i == 0) 
			tmp = i;
	}
	printf("%d\n", tmp);
	printf("%d\n", a * b / tmp);
	return 0;
}