# Ejercicio 3
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
  def lengthOfLIS(self, nums):
    if not nums:
      return 0
    f = [1] * len(nums)
    for i in range(1, len(nums)):
      try:
        f[i] = max(1 + f[j] for j in range(i) if nums[i] > nums[j])
      except:
        f[i] = 1
    return max(f)