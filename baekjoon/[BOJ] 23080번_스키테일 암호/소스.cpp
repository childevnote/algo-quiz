//[BOJ] 23080��_��Ű���� ��ȣ
#include <iostream>
#include <string.h>

using namespace std;
int main()
{
	char n[1000];
	int i, k;

	cin >> k;
	cin >> n;

	for (int i = 0; i < strlen(n); i += k)
		cout << n[i];

	return 0;
}