class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # results = []
        # used = [False] * len(strs)
        # for i in range(len(strs)):
        #     if used[i]:
        #         continue
        #     group = [strs[i]]
        #     used[i] = True
            
        #     for j in range(i + 1, len(strs)):
        #         if not used[j] and Counter(strs[i]) == Counter(strs[j]):
        #             group.append(strs[j])
        #             used[j] = True
        #     results.append(group)
        # return results 

        buckets = {}
        for i, obj in enumerate(strs):
            obj = tuple(sorted(Counter(obj).items()))

            if obj not in buckets:
                buckets[obj] = []
            buckets[obj].append(strs[i])
        return list(buckets.values())
