class Solution {
public:
    bool check(int mid, vector<int>& weights, int days) {
        int value = 0;
        int curr_days = 1;
        for (int j = 0; j < weights.size(); j++) {
            if (value + weights[j] <= mid) {
                value += weights[j];
            } else {
                curr_days++;
                value = weights[j];
                if (value > mid) {
                    return false;
                }
            }
        }
        if (curr_days > days) {
            return false;
        }
        return true;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int n = weights.size();
        int l = *min_element(weights.begin(), weights.end());
        int r = 0;
        for (int j = 0; j < weights.size(); j++) {
            r += weights[j];
        }
        int ans = -1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (check(mid, weights, days)) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return ans;
    }
};