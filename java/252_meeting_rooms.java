import java.util.Arrays;

class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        for (int i = 1; i < intervals.length; i++) {
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];
            int previousStart = intervals[i - 1][0];
            int previousEnd = intervals[i - 1][1];

            if (currentStart >= previousStart && currentStart < previousEnd) {
                return false;
            }
        }

        return true;
    }
}