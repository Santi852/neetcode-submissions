class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        Org = []
        n = len(pairs)
        for i in range(n):
            j = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -= 1
            Org.append(list(pairs))
        return Org