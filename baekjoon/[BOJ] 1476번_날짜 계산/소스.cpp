//[BOJ] 1476��_��¥ ���
#include <iostream>
using namespace std;
int main()
{
	int E, S, M;
	int year = 1;
	cin >> E >> S >> M;
	while (1)
	{
		if ((year - E) % 15 == 0 && (year - S) % 28 == 0 && (year - M) % 19 == 0)
		{
			cout << year << endl;
			break;
		}
		else
			year++;
	}
}

////[BOJ] 1476��_��¥ ���_�ð� �ʰ�
//#include <iostream>
//
//using namespace std;
//
//int main()
//{
//	int E, S, M;
//	int t_E = 1, t_S = 1, t_M = 1;
//	int year = 1;
//
//	cin >> E >> S >> M;
//
//	while (1)
//	{
//		if ((t_E == E) && (t_S == S) && (t_M == M)) {
//			cout << year << endl;
//			break;
//		}
//		else {
//			if (t_E == 16)
//				t_E = t_E - 15;
//			if (t_S == 29)
//				t_S = t_S - 28;
//			if (t_M == 20)
//				t_M = t_M - 19;
//
//			t_E++; t_S++; t_M++; year++;
//		}
//	}
//}