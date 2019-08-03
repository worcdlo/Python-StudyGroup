"""
<Think Python 習題9-8 里程表回文巧合>
	- 從六位數字 100000~ 999996 中, 找出符合以下所有規則的起始數字 
	- 該數字的後四位為Palindrome, ex. 987337
	- 該數字+1之後, 後五位為Palindrome, ex. 987377+1= 987378
	- 該數字+2之後, 中間四位為Palindrome, ex. 835529+2 = 835531
	- 該數字+3之後, 整個數字為Palindrome, ex. 931136+3 = 931139
"""

def GetNumArr(num):
    res = [1] * 6
    for i in range(6):
        res[i] = (int)(num % 10)
        num /= 10
    return res


def FirstPalindrome():
    buff = [0] * 6
    for i in range(100000, 999997):
        #case1
        buff = GetNumArr(i)
        if buff[0] != buff[3] or buff[1] != buff[2] :
            continue
		#case2
        buff = GetNumArr(i + 1)
        if buff[0] != buff[4] or buff[1] != buff[3] :
            continue
		#case3
        buff = GetNumArr(i + 2)
        if buff[1] != buff[4] or buff[2] != buff[3] :
            continue
		#case4
        buff = GetNumArr(i + 3)
        if buff[0] != buff[5] or buff[1] != buff[4] or buff[2] != buff[3]:
            continue
        #print(i, i+1, i+2, i+3)
        return i
    return -1
