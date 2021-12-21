# Ejercicio 1
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid):
    if obstacleGrid[0][0] != 0:
      return 0
    rows, colums = len(obstacleGrid), len(obstacleGrid[0])
    dp = []
    for i in range(rows):
      arr = []
      for j in range(colums):
        arr.append(0)
      dp.append(arr)
    dp[0][0] = 1
    for i in range(rows):
      for j in range(colums):
        if obstacleGrid[i][j] != 0 or (i == 0 and j == 0):
          continue
        if i != 0:
          dp[i][j] += dp[i-1][j]
        if j != 0:
          dp[i][j] += dp[i][j-1]
    return dp[rows-1][colums-1]