#probelm Link : https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        e =0
        odd =[]
        o =0
        ans = []
        for i in range(len(nums)):
            if(i%2):
                odd.append(nums[i])
            else:
                even.append(nums[i])
        even = sorted(even)
        odd = sorted(odd, reverse = True)
        for i in range(len(nums)):
            if(i%2):
                ans.append(odd[o])
                o+=1
            else:
                ans.append(even[e])
                e+=1
        return ans