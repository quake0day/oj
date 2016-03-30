#include <iostream>
#include <vector>
using namespace std;
void SieveofEratosthenes(int n)
{
	//bool prime[n+1];
	//memset(prime, true, sizeof(prime));
	vector<bool> prime(n+1, true);
	for(int p = 2; p*p <=n; p++){
		if(prime[p] == true){
			for(int i = p*2; i<= n; i+=p)
				prime[i] = false;
		}
	}
	for(int p = 2; p <= n; p++)
		if(prime[p])
			cout << p << " ";
	
}


int main()
{
	int n = 100;
	SieveofEratosthenes(n);
	return 0;
}