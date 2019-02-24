"""
最短路徑
"""

def minPathSum(grid):
	m = len(grid)
	n = len(grid[0])
	for i in range(1, n):
		grid[0][i] += grid[0][i - 1]
		
	for i in range(1, m):
		grid[i][0] += grid[i - 1][0]
	
	for i in range(1, m):
		for j in range(1, n):
			grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
	
	return grid[m - 1][n - 1]
	

"""
最大連續子陣列和
"""
def maxSubArray(lt):
	size = len(lt)
	if size == 0:
		return 0
	
	crt, res = lt[0], lt[0]
	
	for i in range(1, size):
		if crt > 0:
			crt += lt[i]
		else:
			crt = lt[i]
			
		if crt > res:
			res = crt
	return res
