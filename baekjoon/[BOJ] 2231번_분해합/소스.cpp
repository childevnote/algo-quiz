////[BOJ]_2231��_������_Ʋ���ڵ�
//#include <iostream>
//using namespace std;
//int main()
//{
//	int n;
//	int tot = 10;
//	int a, b, c, d, e, f;
//
//	cin >> n;
//
//	while (true)
//	{
//		a = tot / 100000;															//10���� �ڸ� ��
//		b = (tot - a * 100000) / 10000;											//���� �ڸ� ��
//		c = (tot - a * 100000 - b * 10000) / 1000;							//õ�� �ڸ� ��
//		d = (tot - a * 100000 - b * 10000 - c * 1000) / 100;				//���� �ڸ� ��
//		e = (tot - a * 100000 - b * 10000 - c * 1000 - d * 100) / 10;	//���� �ڸ� ��
//		f = tot % 10;																//���� �ڸ� ��
//
//		if (tot > n)
//		{
//			cout << "0" << endl;
//			break;
//		}
//		else if ((tot < 100) && (n == tot + e + f))
//		{
//			cout << tot << endl;
//			break;
//		}
//		else if ((tot < 1000) && (n == tot + d + e + f))
//		{
//			cout << tot << endl;
//			break;
//		}
//		else if ((tot < 10000) && (n == tot + c + d + e + f))
//		{
//			cout << tot << endl;
//			break;
//		}
//		else if ((tot < 100000) && (n == tot + b + c + d + e + f))
//		{
//			cout << tot << endl;
//			break;
//		}
//		else if ((tot < 1000000) && (n == tot + a + b + c + d + e + f))
//		{
//			cout << tot << endl;
//			break;
//		}
//		tot++;
//	}
//	return 0;
//}

// [BOJ]_2231��_������
#include <iostream>
using namespace std;
int main()
{
	int n;
	cin >> n;
	int i = n;
	int cnt=0;
	while (i)
	{
		i /= 10;
		cnt++;
	}

	int tot = n - 9 * cnt;
	int num = tot;

	while (true)
	{

		int sum = 0;
		sum += num;
		int x = num;
		while (x)
		{
			sum += (x % 10);
			x /= 10;
		}

		if (num == n) {
			cout << "0" << endl;
			break;
		}

		if (sum == n) {
			cout << num << endl;
			break;
		}
		else
			num++;
	}
	return 0;
}