class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        Map<String, List<Integer>> index = new HashMap<String, List<Integer>>();
        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < wordsDict.length; i++) {
            if (wordsDict[i].equals(word1) || wordsDict[i].equals(word2)) {
                if (index.containsKey(wordsDict[i])) {
                    index.get(wordsDict[i]).add(i);
                } else {
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(i);
                    index.put(wordsDict[i], temp);
                }
            }
        }

        for (int index1 : index.get(word1)) {
            for (int index2 : index.get(word2)) {
                int current = Math.abs(index1 - index2);
                answer = Math.min(answer, current);
            }
        }

        return answer;
    }
}