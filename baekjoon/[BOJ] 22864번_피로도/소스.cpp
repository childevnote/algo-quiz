//[BOJ] 22864��_�Ƿε�
#include<iostream>
using namespace std;
int main()
{
	int fatigue=0, time=0, work=0, rest=0, burnout=0;
	int A, B, C, M;

	cin >> A >> B >> C >> M;

	rest = C;
	burnout = M;

	if (A > M) {
		cout << 0 << endl;
		exit(0);
	}

	while (1)
	{
		fatigue += A;
		if (fatigue > burnout) {
			fatigue -= A;
			fatigue -= rest;
		}
		else
		{
			work+=B;
		}
		time++;

		if (time == 24) {
			cout << work << endl;
			break;
		}
	}
	return 0;
}