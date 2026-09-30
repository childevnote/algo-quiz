//[BOJ] 1934��_�ּҰ����
#include <stdio.h>

int main()
{
	int a, b;
	int i, N = 0;
	int tmp = 0;
	int t;

	scanf("%d", &t);

	if (t < 1 || t>1000)
	{
		printf("�׽�Ʈ ���̽��� ������ ������ϴ�.");
		return;
	}

	while (t)
	{
		scanf("%d %d", &a, &b);
		if (0 > a || a > 45000 || 0 > b || b > 45000) {
			printf("�ڿ����� ������ ������ϴ�.\n");
			return;
		}

		N = (a > b) ? b : a;
		for (i = 1; i <= N; i++)
		{
			if (a % i == 0 && b % i == 0)
				tmp = i;
		}
		printf("%d\n", a * b / tmp);
		t--;
	}
}