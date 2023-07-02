class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x :x[0]-x[1])
        total = len(costs)//2
        cost = 0
        for i in range(total):
            cost += costs[i][0] + costs[total+i][1]
        return cost
    