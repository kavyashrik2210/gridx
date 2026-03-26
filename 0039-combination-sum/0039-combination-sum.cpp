class Solution {
public:
    void backtrack(vector<int>& candidates, int target, int index,
                   vector<int>& path, vector<vector<int>>& result) {

        // Base case
        if (target == 0) {
            result.push_back(path);
            return;
        }

        if (target < 0) return;

        for (int i = index; i < candidates.size(); i++) {
            // Choose
            path.push_back(candidates[i]);

            // Explore (same index allowed)
            backtrack(candidates, target - candidates[i], i, path, result);

            // Backtrack
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> path;

        backtrack(candidates, target, 0, path, result);
        return result;
    }
};