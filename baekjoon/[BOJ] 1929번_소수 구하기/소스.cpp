// [BOJ] 1929��_�Ҽ� ���ϱ�
#include <stdio.h>
int arr[1000001];
int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    arr[0] = 1;
    arr[1] = 1;

    for (int i = 2; i < b + 1; i++)
    {
        for (int j = 2 * i; j < b + 1; j += i) {
            if (arr[j] == 0)
                arr[j] = 1;
        }
    }

    for (int i = a; i < b + 1; i++) {
        if (arr[i] == 0)
            printf("%d\n", i);
    }
    return 0;
}

//// [BOJ] 1929��_�Ҽ� ���ϱ�_�ð��ʰ�
//#include <iostream>
//using namespace std;
//int main() {
//	int a, b;
//	int i, j;
//	cin >> a >> b;
//
//	for (i = a; i <= b; i++) {
//		for (j = 2; j < i; j++)
//		{
//			if (i % j == 0)
//				break;
//		}
//		if (j == i)
//			cout << j << endl;
//	}
//	return 0;
//}