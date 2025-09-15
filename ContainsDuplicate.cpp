#include <iostream>
#include <set>
#include <vector>
using namespace std;

class Solution
{
public:
    bool hasDuplicate(vector<int> &nums)
    {
        set<int> checked;
        for (int i = 0; i < nums.size(); i++)
        {
            if (checked.count(nums[i]))
            {
                return true;
            }
            checked.insert(nums[i]);
        }
        return false;
    };
};
