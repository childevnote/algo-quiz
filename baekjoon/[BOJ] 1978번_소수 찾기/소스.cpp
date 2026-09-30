////[BOJ] 1978��_�Ҽ� ã��
//#include <iostream>
//using namespace std;
//int main()
//{
//	int i, j, N;
//	int num;
//	int tot=0;
//
//	cin >> N;
//	while (N)
//	{
//		cin >> num;
//
//		if (num == 1) {
//			goto pass;
//		}
//		else if (num == 2) {
//			tot++;
//			goto pass;
//		}
//
//		for (j = 2; j < num; j++)
//		{
//			if ((num % j == 0))
//				break;
//			else if (j == num - 1) {
//				tot++;
//				break;
//			}
//		}
//		pass:
//		N--;
//	}
//	cout << tot << endl;
//	return 0;
//}

#include <iostream>

using namespace std;

int main()
{
	int a, b;
	int i, j;
	cin >> a >> b;

	for (i = a; i <= b; i++)
	{
		if (i == 1)
			goto pass;

		else if (i == 2) {
			cout << i << endl;
			goto pass;
		}

		for (j = 3; j < i; j++)
		{
			if (i % j == 0)
				break;
			else if (j == i - 1)
			{
				cout << i << endl;
				break;
			}
		}
	pass:
	}
}