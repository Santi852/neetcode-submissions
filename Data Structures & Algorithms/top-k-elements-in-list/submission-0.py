class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        result = []
        for item ,count in counter.most_common(k):
            result.append(item)
        return result

            

        