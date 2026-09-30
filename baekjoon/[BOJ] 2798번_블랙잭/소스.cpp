//#include <iostream>
//#include <math.h>
//using namespace std;
//
//int main()
//{
//	int N, M, tot = 0, gap=0, index=0;
//	int val[3];
//	int gap_ans=1000;
//	int tot_ans;
//	int index_ans=0;
//	int limit;
//
//	cin >> N >> M;
//
//	limit = pow(N - 2, 3);
//	int* gap_arr = new int[limit];
//	int* tot_arr = new int[limit];
//	int* card = new int[N];
//
//	for (int i = 0; i < N; i++)
//	{
//		cin >> card[i];
//	}
//
//	val[0] = card[0];
//	val[1] = card[1];
//	val[2] = card[2];
//
//	for (int i = 0; i < 3; i++)
//	{
//		tot += val[i];
//	}
//
//	for (int a = 0; a < N; a++)
//	{
//		val[0] = card[a];
//		for (int b = 1; b < N; b++)
//		{
//			if (a == b)
//				continue;
//
//			val[1] = card[b];
//			for (int c = 2; c < N; c++)
//			{
//				if ((b == c)||(a==c))
//					continue;
//
//				tot = 0;
//				gap = 0;
//
//				val[2] = card[c];
//
//				for (int i = 0; i < 3; i++)
//					tot += val[i];
//
//				tot_arr[index] = tot;
//
//				gap = M - tot;
//
//				if (gap < 0) 
//					gap *= -1;
//
//				gap_arr[index] = gap;
//
//				if (gap_ans > gap_arr[index]) {
//					gap_ans = gap_arr[index];
//					index_ans = index;
//				}
//
//				tot_ans = tot_arr[index_ans];
//
//				for (int j = 0; j < 3; j++)
//					cout << val[j] << " ";
//
//				cout << "gap : " << gap << " ";
//				cout << "tot : " << tot << " ";
//				cout << "index : " << index << endl;
//				cout << endl;
//
//				index++;
//			}
//		}
//	}
//	cout << endl;
//	cout << "index_ans : " << index_ans << endl;
//	cout << tot_ans << endl;
//
//	return 0;
//}

//[BOJ] 2798��_������
#include <iostream>
using namespace std;

int main()
{
	int N, M;
	int tot =0,tot_ans=0;

	cin >> N >> M;

	int* card = new int[N];

	for (int i = 0; i < N; i++)
	{
		cin >> card[i];
	}


	for (int a = 0; a < N-2; a++)
	{
		for (int b = a+1; b < N-1; b++)
		{
			for (int c = b+1; c < N; c++)
			{
				tot = card[a] + card[b] + card[c];
				if (tot > tot_ans && tot <= M)
					tot_ans = tot;
			}
		}
	}
	cout << tot_ans << endl;

	return 0;
}