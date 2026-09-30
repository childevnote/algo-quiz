//[BOJ] 10872��_���丮��
#include <iostream>
using namespace std;
int main()
{
	int N;
	int F=1;

	cin >> N;

	if ((N < 0) || (N > 12)) {
		cout << "���� N�� ����(0 �� N �� 12)���� ������ϴ�." << endl;
		exit(1);
	}

	while (N) {
		F = F * N;
		N--;
	}

	cout << F << endl;
	return 0;
}