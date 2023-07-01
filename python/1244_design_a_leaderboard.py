class Leaderboard:
    def __init__(self):
        self.dic = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.dic:
            self.dic[playerId] = 0
        self.dic[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for x in self.dic.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        result = 0
        while heap:
            result += heapq.heappop(heap)
        return result

    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0
