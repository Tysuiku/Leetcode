# 1
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


# 121
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            val = price - minPrice
            if price < minPrice:
                minPrice = price
            elif val > maxProfit:
                maxProfit = val
        return maxProfit


# 217
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        val = {}
        for num in nums:
            if num in val:
                return True
            else:
                val[num] = 1
        return False


# 53
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum


# 152
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            result = max(result, max_prod)

        return result


# 242
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = self.anaHash(s)
        map2 = self.anaHash(t)
        return map1 == map2

    def anaHash(self, str):
        ana_map = {}
        for char in str:
            if char in ana_map:
                ana_map[char] += 1
            else:
                ana_map[char] = 1
        return ana_map
