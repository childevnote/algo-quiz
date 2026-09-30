////[BOJ] 17427��_����� �� 2_�ð� �ʰ�
//#include <iostream>
//using namespace std;
//int main()
//{
//	int N;
//	long long tot = 0;
//
//	cin >> N;
//	if ((N < 1) || (N > 1000000)) {
//		cout << "N�� ������ ������ϴ�." << endl;
//		exit(1);
//	}
//
//	for (int i = 1; i <= N; i++) {
//		//i�� ����� ���� ���ϴ� �˰�����
//		for (int j = 1; j <= i; j++) {
//			if (i % j == 0) {
//				tot += j;
//			}
//		}
//	}
//
//	cout << tot << endl;
//	return 0;
//}

//[BOJ] 17427��_����� �� 2
#include <iostream>
using namespace std;
int main()
{
	int N;
	long long tot = 0;

	cin >> N;
	if ((N < 1) || (N > 1000000)) {
		cout << "N�� ������ ������ϴ�." << endl;
		exit(1);
	}

	for (int i = 1; i <= N; i++) 
		tot += (N / i) * i;

	cout << tot << endl;
	return 0;
}