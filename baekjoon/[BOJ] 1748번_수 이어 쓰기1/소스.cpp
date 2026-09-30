//#include <iostream>
//using namespace std;
//int main()
//{
//	int count = 0;
//	int n; cin >> n;
//	for (int i = 1; i <= n; i++)
//	{
//		if (i < 10)
//			count++;
//		else if (i < 100)
//			count = count + 2;
//		else if (i < 1000)
//			count = count + 3;
//		else if (i < 10000)
//			count = count + 4;
//		else if (i < 100000)
//			count = count + 5;
//		else if (i < 1000000)
//			count = count + 6;
//		else if (i < 10000000)
//			count = count + 7;
//		else if (i < 100000000)
//			count = count + 8;
//	}
//	cout << count << endl;
//}

//#include <iostream>
//#include <string>
//using namespace std;
//int main()
//{
//	int count = 0;
//	int tot;
//	int n; cin >> n;
//	string all;
//	for (int i = 1; i <= n; i++)
//	{
//		string s = to_string(i);
//		all += s;
//	}
//	cout << endl;
//	tot = stoi(all);
//
//	while (1)
//	{
//		count++;
//		tot /= 10;
//		if (tot < 1)
//			break;
//	}
//
//	cout << count << endl;
//}

////[BOJ] 1748��_�� �̾� ����1_�޸� �ʰ�
//#include <iostream>
//#include <sstream>
//using namespace std;
//int main()
//{
//	int n; cin >> n;
	//if (n < 1 || n>100000000)
	//{
	//	cout << "n�� ������ ������ϴ�." << endl;
	//	exit(1);
	//}
//	string all;
//	for (int i = 1; i <= n; i++)
//	{
//		string s = to_string(i);
//		all.append(s);
//	}
//	cout << all.length() << endl;
//	return 0;
//}


////[BOJ] 1748��_�� �̾� ����1
//#include<cstdio>
//int n, r;
//int main() {
//	scanf("%d", &n);
//	for (int i = 1; i <= n; i *= 10)
//		r += n - i + 1;
//	printf("%d", r);
//	return 0;
//}