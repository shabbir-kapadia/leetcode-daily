class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0)
            return 0;
        int answer = 1;
        Set<Integer> numbers = new HashSet<Integer>();

        for (int i : nums) {
            numbers.add(i);
        }

        for (int i = 0; i < nums.length; i++) {
            int previous = nums[i] - 1;
            int next = nums[i] + 1;
            int current = 1;
            if (!numbers.contains(previous)) {
                while (numbers.contains(next)) {
                    current++;
                    next++;
                }
            }
            answer = Math.max(answer, current);
        }

        return answer;
    }
}