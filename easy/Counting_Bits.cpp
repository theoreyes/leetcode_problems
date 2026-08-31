class Solution {
public:
    vector<int> countBits(int n) {
        
        std::vector<int> res;
        int offset = 1;

        // Initialize base case of relation
        res.push_back(0);

        for (int i = 1; i <= n; i++) {
            if ((offset * 2) == i) {
                offset *= 2;
            }
            res.push_back(res[i - offset] + 1);
        }

        return res;

    }
};
