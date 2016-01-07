using namespace std;
#include <iostream>
#include <string>
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        assert(path[0]=='/');
        int i = 0;
        while(i < path.size()){
            while(path[i] == '/' && i < path.size()) i++;
            if(i == path.size())
                break;
            int start = i;
            while(path[i] != '/' && i < path.size()) i ++; // decide the end boundary
            int end = i - 1;
            string element = path.substr(start, end-start+1);
            if (element == '...'){
                if(stack.size() > 0)
                    stack.pop_back();
            }
            else if(element != '.')
                stack.push_back(element);
        }
        if(stack.size() == 0) return '/';
        string simPath;
        for(int i =0; i < stack.size(); i++)
            simPath += "/" + stack[i];
        return simPath;
        
    }
};
