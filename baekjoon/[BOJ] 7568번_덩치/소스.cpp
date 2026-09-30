//[BOJ] 7568��_��ġ
#include <iostream>
using namespace std;
int main()
{
	int n;

	cin >> n;

	int** arr = new int* [n];

	for (int i = 0; i < n; i++) //2Xn �迭 ����
	{
		arr[i] = new int[2];
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < 2; j++)
			cin >> arr[i][j];
	}

	int* rate = new int[n]; //������ ���� �迭 ����

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < 2; j += 2) //j�� �ΰ��� �ǳʶپ� �����Կ� Ű�� �ϳ��� �������� �ν�
		{
			rate[i] = 1; //������ �� ��ġ�� ���������� 1�� �ʱ�ȭ
			for (int k = 0; k < n; k++)
			{
				for (int l = 0; l < 2; l += 2)
				{
					if ((arr[i][j] < arr[k][l]) && (arr[i][j + 1] < arr[k][l + 1]))
						rate[i]++; //�ڽź��� ū ��ġ�� ���� ��� ������ 1 ����
				}
			}
		}
	}

	for (int i = 0; i < n; i++) //������� ������ ���� ���
		cout << rate[i] << " ";

	return 0;
}