#include "lc.h"

class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        int ones = ~0;
        int mask = 0;
        if (j < 31) {
            int left = ones << (j + 1);
            int right = ((1 << i) - 1);
            mask = left | right;
        } else {
            mask = (1 << i) - 1;
        }

        return (n & mask) | (m << i);
    }
};


int main(int argc, char const *argv[]) {
	Solution sol;

	cout << sol.updateBits(-521, 0, 31, 31) << endl;
	cout << sol.updateBits(1024,21,2,6) << endl;

	return 0;
}
