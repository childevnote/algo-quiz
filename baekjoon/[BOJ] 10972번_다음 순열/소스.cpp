//[BOJ] 10972��_���� ����
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int N;

	cin >> N;
	if ((N < 1) || (N > 10000))
	{
		cout << "N�� ������ ������ϴ�." << endl;
		exit(1);
	}

	int* str = new int[N];

	for (int i = 0; i < N; i++)
	{
		cin >> str[i];
	}

	if (next_permutation(str, str + N))
	{
		for (int i = 0; i < N; i++) {
			cout << str[i] << " ";
		}
	}
	else
		cout << "-1" << endl;

	return 0;
}