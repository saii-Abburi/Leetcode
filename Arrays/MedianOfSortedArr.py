#problem link : https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans= []
        n1 = len(nums1)
        n2 = len(nums2)
        mid = (n1+n2)//2
        i =0
        j =0
        while(i< n1 and j< n2):
            if(nums1[i]>nums2[j]):
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
        while(i<n1):
            ans.append(nums1[i])
            i+=1
        while(j<n2):
            ans.append(nums2[j])
            j+=1
        if((n1+n2)%2>0):
            return ans[mid]
        else:
            return (ans[mid-1]+ans[mid])/2
        return -1
    