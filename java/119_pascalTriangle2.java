class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();

        for (int i = 0; i < rowIndex + 1; i++) {
            List<Integer> temp = new ArrayList<Integer>();
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    temp.add(1);
                } else {
                    temp.add(answer.get(i - 1).get(j - 1) + answer.get(i - 1).get(j));
                }
            }
            answer.add(temp);
        }

        return answer.get(rowIndex);

    }
}