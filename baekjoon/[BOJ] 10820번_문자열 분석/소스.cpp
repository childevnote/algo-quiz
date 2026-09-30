//[BOJ] 10820��_���ڿ� �м�
#include <iostream>
#include <string.h>
#define SIZE 100
using namespace std;

int main()
{
	while (1)
	{
		int i = 0;
		int upper = 0, lower = 0, num = 0, blank = 0;
		char str[SIZE + 1];
		cin.getline(str, SIZE+1);

		if (strlen(str) == 0)
			return 0;

		while (str[i] != '\0')
		{
			if (str[i] >= 'a' && str[i] <= 'z')
				lower++;
			else if (str[i] >= 'A' && str[i] <= 'Z')
				upper++;
			else if (str[i] >= '0' && str[i] <= '9')
				num++;
			else if (str[i] == ' ')
				blank++;
			i++;
		}
		cout << lower << " " << upper << " " << num << " " << blank << endl;
	}
	return 0;
}