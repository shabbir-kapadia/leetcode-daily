class Solution {
    public boolean isUgly(int n) {
        if (n <= 0) {
            return false;
        }

        int[] prime = new int[] { 2, 3, 5 };

        for (int i : prime) {
            n = keepDividing(n, i);
        }

        return n == 1;
    }

    public int keepDividing(int n, int prime) {
        while (n % prime == 0) {
            n /= prime;
        }

        return n;
    }
}