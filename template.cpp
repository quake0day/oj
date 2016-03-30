#include <iostream>

using namespace std;


template <class T>
T biggest(T a, T b)
{
	return a > b ? a :b;
}

int main()
{
	cout <<"biggest"<<biggest(10,15)<<endl;
	cout << biggest('k','s')<<endl;
	return 0;
}