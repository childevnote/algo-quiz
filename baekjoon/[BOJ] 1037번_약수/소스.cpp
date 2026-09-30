//[BOJ] 1037��_���
#include <iostream>
using namespace std;
int main()
{
	int N;
	int min=0, max=0;
	int val=0;

	cin >> N;
	int* A = new int[N];

	if(N>50) {
		cout << "N�� 50���� �۰ų� ���ƾ� �մϴ�." << endl;
		exit(1);
	}

	for (int i = 0; i < N; i++)
	{
		cin >> A[i];

		if ((A[i]<2)||(A[i]>1000000)) {
			cout << "��¥ ����� 2���� ũ�ų� ���� 1000000���� �۰ų� ���ƾ� �մϴ�." << endl;
			exit(1);
		}
	}

	min = A[0];
	max = A[0];

	for (int i = 0; i < N; i++)
	{
		if (A[i] > max)
			max = A[i];
		if (A[i] < min)
			min = A[i];
	}

	val = min * max;
	cout << val << endl;
	return 0;
}