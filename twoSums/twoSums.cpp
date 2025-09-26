#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> dict;
        int difference;

        for (int i = 0; i < nums.size(); i++)
        {
            difference = target - nums[i];
            if (dict.count(difference))
            {
                return {dict[difference],i};
            }
            dict[nums[i]] = i;
        }
        return {};
    }
};


