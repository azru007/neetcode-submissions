class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return set(nums.sort())[-k:]
        coun = Counter(nums)
        coun = dict(sorted(coun.items(), key=lambda i:i[1], reverse=True))
        return list(coun.keys())[:k]