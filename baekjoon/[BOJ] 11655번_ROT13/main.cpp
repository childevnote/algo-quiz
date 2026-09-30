//#include <iostream>
//#define SIZE 100
//using namespace std;
//
//int main() {
//
//	int i = 0;
//	char S[SIZE];
//	cin.getline(S, SIZE+1);
//
//	while (!(S[i] == '\0'))
//	{
//		if (S[i] >= 'A' && S[i] <= 'Z')
//		{
//			if (S[i] + 13 > 90)
//				cout << (S[i] - 13);
//			else
//				cout << S[i] + 13;
//		}
//		else if (S[i] >= 'a' && S[i] <= 'z')
//		{
//			if (S[i] + 13 > 122)
//				cout << (S[i] - 13);
//			else
//				cout << S[i] + 13;
//		}
//		else
//			cout << S[i];
//		i++;
//	}
//}

//[BOJ] 11655��_ROT13
#include <iostream>
#include <stdio.h>
#define SIZE 100
using namespace std;

int main() {

	int i = 0;
	char S[SIZE];
	cin.getline(S, SIZE + 1);

	while (!(S[i] == '\0'))
	{
		if (S[i] >= 'A' && S[i] <= 'Z')
		{
			if (S[i] + 13 > 90)
				printf("%c", S[i] - 13);
			else
				printf("%c", S[i] + 13);
		}
		else if (S[i] >= 'a' && S[i] <= 'z')
		{
			if (S[i] + 13 > 122)
				printf("%c", S[i] - 13);
			else
				printf("%c", S[i] + 13);
		}
		else
			cout << S[i];
		i++;
	}
}