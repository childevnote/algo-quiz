////[BOJ] 11655��_���μ�����_�ð��ʰ�����
//#include <iostream>
//using namespace std;
//int main()
//{
//	int N;
//	int x = 2;
//	cin >> N;
//
//	while (1)
//	{
//		if (N % x == 0) {
//			N = N / x;
//			cout << x << endl;
//		}
//		else if (N == x)
//			break;
//		else
//			x++;
//	}
//	return 0;
//}

//[BOJ] 11655��_���μ�����
#include <iostream>
using namespace std;
int main()
{
	int N;
	int x = 2;
	cin >> N;

	while (1)
	{
		if (N == 1) {
			break;
		}
		else if (N % x == 0) {
			N = N / x;
			cout << x << endl;
		}
		else
			x++;
	}
	return 0;
}