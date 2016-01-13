class Solution {
public:
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    vector<int> mergeSortedArray(vector<int> &A, vector<int> &B) {
        // write your code here
        std::vector<int> C;
        int i = 0, j = 0;
        while(i < A.size() && j < B.size()){
        	if (A[i] < B[j]){
        		C.push_back(A[i++]);
        	}
        	else{
        		C.push_back(B[j++]);
        	}
        }
        while (i < A.size()){
        	C.push_back(A[i++]);
        }
        while (j < B.size()){
        	C.push_back(B[j++]);
        }
        return C;
    }
};
