class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # freq = {}
        # # hashmap to store the freq of the nums
        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 0
        #     freq[num] += 1
        # bucket sort
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        print(bucket)
        ans = []
        # pick the "k" amount of numbers with top freq
        # range(starting point, ending point, step)
        # => starting point: len - 1; ending point: -1; step: -1
        for i in range(len(bucket) - 1, -1, -1):            
            for value in bucket[i]:
                if len(ans) >= k:
                    break
                ans.append(value)
        
        return ans