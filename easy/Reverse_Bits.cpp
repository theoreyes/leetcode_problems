class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        
        uint32_t res = 0;
        uint32_t NUM_WIDTH = 32;

        for (int i = 0; i < NUM_WIDTH; i++) {
            
            if ((n >> i) & 1) {
                res |= (1u << (31 - i));
            }

        }

        return res;

    }
};
