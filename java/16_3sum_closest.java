import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int answer = Integer.MAX_VALUE;
        int difference = Integer.MAX_VALUE;

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            int low = i + 1;
            int high = nums.length - 1;
            while (low < high) {
                int sum = nums[i] + nums[low] + nums[high];
                if (Math.abs(target - sum) < difference) {
                    difference = Math.abs(target - sum);
                    answer = sum;
                }
                if (sum < target) {
                    low++;
                } else {
                    high--;
                }
            }
        }

        return answer;
    }
}