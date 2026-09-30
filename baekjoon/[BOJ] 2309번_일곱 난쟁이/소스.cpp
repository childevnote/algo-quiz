//[BOJ] 2309��_�ϰ� ������
#include <iostream>
using namespace std;

int main()
{
	int length[10];
	int tot = 0;
	int index1 = 0;
	int index2 = 0;
	int temp = 0;

	for (int i = 0; i < 9; i++)
	{
		cin >> length[i];
		if (length[i] > 100)
		{
			cout << "�������� Ű�� 100�� ���� �� �����ϴ�." << endl;
			break;
		}
	}

	cout << endl;

	for (int i = 0; i < 9; i++) {
		tot = tot + length[i];
	} //tot�� �����̵��� Ű�� �� ���� ���� �����Ѵ�.

	for (int a = 0; a < 9; a++)
	{
		for (int b = 0; b < 9; b++)
		{
			if (tot - (length[a] + length[b]) == 100)
			{
				index1 = a;
				index2 = b;
				break;
			}
		}
	} //��� ����� ���� ���� �����̵��� Ű ���տ��� 
	  //�� �������� Ű�� �� ���� 100�� �Ǵ� ������ �ε����� �����Ѵ�.

	for (int i = index1; i < 9; i++)
	{
		length[i] = length[i + 1];
	} //index1��°���� �ε����� 1 �������� length[index1]�� �����Ѵ�.

	for (int i = index2; i < 8; i++)
	{
		length[i] = length[i + 1];
	} //index2��°���� �ε����� 1 �������� length[index2]�� �����Ѵ�.

	for (int x = 0; x < 6; x++)
	{
		for (int y = 0; y < 6 - x; y++)
		{
			if (length[y] > length[y + 1]) {
				temp = length[y];
				length[y] = length[y + 1];
				length[y + 1] = temp;
			}
		}
	} //length�迭�� ���� ������������ �����Ѵ�.

	for (int i = 0; i < 7; i++)
	{
		cout << length[i] << endl;
	}
	cout << endl;
	return 0;
}