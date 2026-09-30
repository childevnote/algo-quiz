////[BOJ] 9012_��ȣ 
//#include <iostream> 
//#include <stack> 
//#include <string> 
//using namespace std;
//int main() {
//    int i, j, size;
//    int T = 0;
//    cin >> T;
//    for (i = 0; i < T; i++) {
//        string str;
//        string ans = "YES";
//        cin >> str;
//        stack<char> s;
//        for (j = 0; j < str.length(); j++) {
//            if (str[j] == '(')
//                s.push(str[j]);
//            else if (!s.empty() && (str[j] == ')'))
//                s.pop();
//            else {
//                ans = "NO";
//                break;
//            }
//        }
//        if (!s.empty())
//            ans = "NO";
//        cout << ans << endl;
//    } return 0;
//}

////[BOJ] 9012_��ȣ_��Ÿ�ӿ��� 
//#include <iostream> 
//#include <stack> 
//#include <string> 
//using namespace std;
//int Func() {
//    string str;
//    cin >> str;
//    stack<char> s;
//    for (int j = 0; j < str.length(); j++) {
//        if (str[j] == '(')
//            s.push(str[j]);
//        else if (!s.empty() && (str[j] == ')'))
//            s.pop();
//        else
//            return false;
//    }
//    if (!s.empty())
//        return false;
//}
//
//
//int main() {
//    int T = 0;
//    cin >> T;
//    for (int i = 0; i < T; i++) {
//        if (!Func())
//            cout << "NO" << endl;
//        else
//            cout << "YES" << endl;
//    }
//    return 0;
//}