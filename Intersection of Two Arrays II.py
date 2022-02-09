class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1 = {}
        for num in nums1:
            hashmap1[num] = hashmap1.get(num,0)+1
        res = []
        for num in nums2:
            flag = hashmap1.get(num, 0)
            if flag:
                res.append(num)
                hashmap1[num] -= 1
        return res
