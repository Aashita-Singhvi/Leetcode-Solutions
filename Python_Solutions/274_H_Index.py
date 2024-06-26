class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if (citations[0] == 0): return 0
        for i in range(len(citations)):
            if citations[i] < i+1: return i
        return len(citations)