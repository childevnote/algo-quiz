#include <iostream>
#include <stdlib.h>
using namespace std;

typedef struct Student {
	int num = 0;
	int class_num = 0;
	char name[16] = " ";
};

int main()
{
	Student *stu = new Student;
	int N, M;

	cin >> N >> M;

	int i = 0;
	while (true)
	{
		cin >> stu[i].class_num >> stu[i].name;
		if(i>0)
		{
			for (int j = 0; j < i; j++)
			{
				if (stu[i].class_num == stu[j].class_num)
					stu[i].num++;
			}

			/*if (stu[i].class_num < stu[i - 1].class_num)
			{
				int tmp = stu[i].class_num;
				stu[i].class_num = stu[i-1].class_num;
				stu[i - 1].class_num = tmp;
			}*/
		}
		if (stu[i].class_num == 0 || stu[i].name == 0)
			break;
		i++;
	}

	cout << endl;

	for (int j = 0; j < i; j++)
	{
		if (stu[j].num <= M)
			cout << stu[j].class_num << " " << stu[j].name << endl;
	}




	delete stu;
	return 0;
}