//[BOJ] 2884�� �˶� �ð�
#include<iostream>
using namespace std;
int main()
{
	int h, m;

	cin >> h >> m;

	if (m - 45 < 0)
	{
		h--;
		if (h < 0)
			h += 24;
		m = 60 + (m - 45);
	}

	else
		m -= 45;

	cout << h << " " << m << endl;
}