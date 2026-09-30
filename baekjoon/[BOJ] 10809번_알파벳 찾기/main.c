//[BOJ] 10809��_���ĺ� ã��
#include <stdio.h>

int main(void)
{
	char S[101];
	int i;
	scanf("%s", S);

	for (int a = 97; a<=122; a++)
	{
		i = 0;
		while (S[i]!=0)
		{
			if ((char)a == S[i])
				break;
			i++;
		}
		if ((char)a == S[i])
			printf("%d ", i);
		else
			printf("-1 ");
	}
	return 0;
}
