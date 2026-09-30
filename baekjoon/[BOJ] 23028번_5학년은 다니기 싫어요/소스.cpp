//[BOJ] 23028��_5�г��� �ٴϱ� �Ⱦ��
#include <iostream>
using namespace std;
int main()
{
	int N, A, B;
	int X, Y;
	int major = 0, non_major = 0, tot = 0, semester = 0;
	tot = major + non_major;
	cin >> N >> A >> B;

	for (int i = 0; i < 10; i++)
	{
		cin >> X >> Y;
		for (int j = 0; j < X+Y; j++) {
			if (j == 6)
				break;
			else if (j >= X)
				non_major += 3;
			else
				major += 3;
		}

		semester++;
		tot = major + non_major;

		if ((A + major >= 66) && (B + tot >= 130))
		{
			cout << "Nice" << endl;
			break;
		}

		if (N + semester == 8)
		{
			cout << "Nae ga wae" << endl;
			break;
		}
	}
	return 0;
}