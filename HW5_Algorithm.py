"""
run length壓縮
"""


def RLCompress(chars):
	tmpChar = chars[0] #需假定chars非空
	cnt = rLen = 0
	for c in chars:
		if c != tmpChar:
			chars[rLen] = tmpChar
			rLen += 1
			if cnt > 1:                  
				numStr = str(cnt)#有看過直接轉成list蓋掉原本chars
				for n in numStr:
					chars[rLen] = n
					rLen += 1
			tmpChar = c
			cnt = 1
		else:
			cnt += 1 
			
	chars[rLen] = tmpChar
	rLen += 1
	if cnt > 1:              
		numStr = str(cnt) 
		for n in numStr:
			chars[rLen] = n
			rLen += 1
	return rLen
        
		
"""
奇偶排序
"""

def SortArry(A):
	n = len(A)
	i = 0
	j = 1
	while 1:
		while i < n and A[i] & 1 == 0:
			i += 2

		while j < n and A[j] & 1 == 1:
			j += 2

		if i >= n or j >= n:
			break

		A[i], A[j] = A[j], A[i]
		i += 2
		j += 2
	return A
