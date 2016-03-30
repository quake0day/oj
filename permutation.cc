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
vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret = {{}};
        for (int n : nums){
            vector<vector<int>> temp;
            for (auto x : ret){
                for (int i = 0; i <= x.size(); i++){
                    vector<int> t = x;
                    t.insert(t.begin() + i, n);
                    temp.push_back(t);
                }
            }
            ret.swap(temp);
        }
        return ret;
    }
    
};

int main(){
    Solution *a = new Solution();
    //vector<string> res = a->fizzBuzz(0);
    vector<int> c = {1,2,3};
    vector<vector<int>> res = a->permute(c);
    for (auto i= res.begin(); i != res.end(); i++)
        for(auto j = *i->begin(); j != *i->end(); j++)
                std::cout << j << " ";
    //for (auto i = path.begin(); i != path.end(); ++i)
    //std::cout << *i << ' ';
}