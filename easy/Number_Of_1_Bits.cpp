class Solution {
public:
    int hammingWeight(uint32_t n) {

        int NUM_BITS = 32;
        uint32_t mask = 1;
        int res = 0;

        for (int i = 0; i < NUM_BITS; i++) {
            if (mask & n) {
                res += 1;
            }
            mask = mask << 1;
        }

        return res;

    }
};
