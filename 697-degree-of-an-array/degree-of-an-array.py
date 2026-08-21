class Solution(object):
    def findShortestSubArray(self, nums):
        freq = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            num = nums[i]

            freq[num] = freq.get(num, 0) + 1
            first[num] = first.get(num, i)
            last[num] = i

        degree = max(freq.values())
        answer = float('inf')

        for num in freq:
            if freq[num] == degree:
                answer = min(answer, last[num] - first[num] + 1)

        return answer