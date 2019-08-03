"""
格雷碼
"""

def grayCode(n):
	if n < 1:
		return [0]
	
	offset = 2 
	totalLen = 2 << (n - 1);
	
	lst = [0] * totalLen
	lst[1] = 1
	
	while offset < totalLen:
		for i in range(offset):
			lst[offset + i] = lst[offset - i - 1] | offset
		offset <<= 1
	return lst

"""
爬樓梯
DP問題
"""

def climbStairs(n):
	tmp = 1
	res = 1
	for i in range(1,n):
		res += tmp
		tmp = res - tmp
	return res
