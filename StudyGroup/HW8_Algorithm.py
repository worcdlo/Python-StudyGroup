"""
permutation
給一個list
排列出所有長度為M的組合
"""
def pnm(lt, M):
    lt2 = []
    permutation3(lt, 0, M, lt2)
    return lt2

def permutation3(lt, idx, M, lt2):
    if(idx < M):
        permutation3(lt, idx + 1, M, lt2)
        for i in range(idx + 1, len(lt)):
            lt[idx], lt[i] = lt[i], lt[idx]
            permutation3(lt, idx + 1, M, lt2)
            lt[idx], lt[i] = lt[i], lt[idx]
    else:
        lt2.append(''.join(lt[0:M]))

		
"""
nQueen
"""
def nqueen(N):
    buffSize = 2 * N - 1
    buffShift = N - 1

    res = []
    stack = [-1] * N
    colHt = [0] * N
    lSlopeHt = [0] * buffSize
    rSlopeHt = [0] * buffSize
    
    row ,cnt = 0, 0
    while row > -1:

        j = stack[row]
        if j != -1:
            ResetIJ(row , j, colHt, lSlopeHt, rSlopeHt, buffShift)

        j += 1
        while j < N and CheckHt(row , j, colHt, lSlopeHt, rSlopeHt, buffShift):
            j += 1

        if j == N:
            stack[row] = -1
            row -= 1
        elif row == buffShift:
            cnt += 1
            row -= 1
        else:
            SetIJ(row , j, colHt, lSlopeHt, rSlopeHt, buffShift)
            stack[row] = j
            row += 1

    return cnt
	
def SetIJ(i , j, colHt, lSlopeHt, rSlopeHt, rShift):
    colHt[j] = 1
    lSlopeHt[i + j] = 1
    rSlopeHt[j - i + rShift] = 1

def ResetIJ(i , j, colHt, lSlopeHt, rSlopeHt, rShift):
    colHt[j] = 0
    lSlopeHt[i + j] = 0
    rSlopeHt[j - i + rShift] = 0

def CheckHt(i , j, colHt, lSlopeHt, rSlopeHt, rShift):
    if colHt[j] == 1:
        return True
    if lSlopeHt[i + j] == 1:
        return True
    if rSlopeHt[j - i + rShift] == 1:
        return True
    return False
	
"""
lSlopeHtS[9] = [1,0,0,0,0,0,0,0,1]
代表下圖中，0的斜線上、8的斜線上有Q

0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8

同理，變成往右下斜線
rSlopeHtS[5]
4 5 6 7 8
3 4 5 6 7
2 3 4 5 6
1 2 3 4 5
0 1 2 3 4
"""
