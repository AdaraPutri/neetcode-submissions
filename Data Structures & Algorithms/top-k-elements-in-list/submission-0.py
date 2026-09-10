class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            if counter[n] == 0:
                counter[n] = 1
            else:
                counter[n] += 1
        output_arr = []
        for i in range(k):
            a = max(counter, key = counter.get)
            output_arr.append(a)
            counter.pop(a)
        return output_arr
        