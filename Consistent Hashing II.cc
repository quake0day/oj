class Solution {
public:
    // @param n a positive integer
    // @param k a positive integer
    // @return a Solution object
    template<typename T>
    void swap(T &a, T &b)
    {
        T t = a;
        a = b;
        b = t;
    }

    static Solution create(int n, int k) {
        // Write your code here
        int nn = n;
        int kk = k;
        vector<int> v = {};
        for(auto i = 0; i < nn; i++){
            v.push_back(i);
        }
        for(auto i = 0; i < nn; i++){
            int r = i + std::rand() % (nn - i + 1);
            swap(v[i], v[r]);
        }
        unordered_map<int, int> h;
    }

    // @param machine_id an integer
    // @return a list of shard ids
    vector<int> addMachine(int machine_id) {
        // Write your code here
        vector<int> res = {};
        for (auto i = 0; i < kk; i++){
            res.push_back(v.pop_back());
        }
        for(auto n : res)
        {
            h[n] = machine_id;
        }
        return res;
    }

    // @param hashcode an integer
    // @return a machine id
    int getMachineIdByHashCode(int hashcode) {
        // Write your code here
        while (h.find(hashcode) == h.end()){
            hashcode ++;
        }
        return h[hashcode];
    }
};
