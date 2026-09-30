#include <iostream>

using namespace std;

int rear = 0;
int front = 0;

bool isFull(int N);
bool isEmpty();
int deQueue(int N, int* Q, int K);
void enQueue(int i, int N, int* Q);

int main()
{
	int N, K;

	cin >> N;
	cin >> K;

	int* Q = new int[N];

	for (int i = 0; i < N; i++)
	{
		enQueue(i, N, Q);
	}

	cout << "<" << Q[rear];
	while (!isEmpty())
	{
		cout << ", " << deQueue(N, Q, K);
	}
	cout << ">" << endl;

	delete[] Q;
	
	return 0;
}

bool isFull(int N)
{
	if ((rear + 1) % N == front)
		return true;
	else
		return false;
}

bool isEmpty()
{
	if (front == rear)
		return true;
	else
		return false;
}

void enQueue(int i, int N, int*Q)
{
	if (isFull(N))
	{
		cout << "Queue is Full" << endl;
		exit(1);
	}
	else
	{
		rear = (rear + 1) % N;
		Q[rear] = i;
	}
}

int deQueue(int N, int*Q, int K)
{
	if (isEmpty())
	{
		cout << "Queue is Empty" << endl;
		exit(1);
	}
	else
	{
		front = (front + 1)%N;
		return Q[front+K];
	}
}
