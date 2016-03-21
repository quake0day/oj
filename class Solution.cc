#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    /**
     * param n: As description.
     * return: A list of strings.
     */
    vector<string> fizzBuzz(int n) {
       
                vector<string> results;
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                results.push_back("fizz buzz");
            } else if (i % 5 == 0) {
                results.push_back("buzz");
            } else if (i % 3 == 0) {
                results.push_back("fizz");
            } else {
                results.push_back(to_string(i));
            }
        }
        return results;

    }
    
};

int main(){
    Solution *a = new Solution();
    vector<string> res = a->fizzBuzz(0);
    for (auto i= res.begin(); i != res.end(); i++)
        std::cout << *i << " ";
    //for (auto i = path.begin(); i != path.end(); ++i)
    //std::cout << *i << ' ';
}