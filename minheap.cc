#include <queue>
#include <string>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <array>
using namespace std;

struct  comparator
{
	bool operator()(int i, int j){
		return i > j;
	}
	
};

int main(int argc, char const *argv[])
{
	priority_queue<int, std::vector<int>, comparator> minHeap;
	std::array<int, 3> a1{ {1, 2, 3} };
	for(int i = 0; i < a1.size(); i++){
		minHeap.push(a1[i]);
	}
	minHeap.push(10);
	minHeap.push(5);
	minHeap.push(12);
	minHeap.push(3);
	minHeap.push(3);

	while(!minHeap.empty()){
		cout << minHeap.top() << " ";
		minHeap.pop();
	}
	return 0;
}