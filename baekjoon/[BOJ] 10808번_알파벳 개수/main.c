//[BOJ] 10808��_���ĺ� ����
#include <stdio.h>
#include <string.h>

int main()
{
	char S[101];
	int i, j;
	scanf("%s", S);

	for (i = 0; i < strlen(S); i++)
	{
		if (!(S[i] >= 97 && S[i] <= 122))
			exit(1);
	}

	for (i = 97; i <= 122; i++)
	{
		int num = 0;
		for (j = 0; j < strlen(S); j++)
		{
			if (S[j] == i)
				num++;
		}
		printf("%d ", num);
	}
	printf("\n");
	return 0;
}