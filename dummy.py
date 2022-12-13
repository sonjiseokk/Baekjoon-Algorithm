from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        candidates.sort()
        res = []
        def backtrack(target,candidates):
            if target == 0:
                res.append(arr[:])
                return
            
            for i, x in enumerate(candidates):
                if x <= target:
                    arr.append(x)
                    backtrack(target-x,candidates[i::])
                    arr.pop()
        
        backtrack(target, candidates)

        return res

a =Solution()
print(a.combinationSum([2,3,6,7],7))
