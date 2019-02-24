'''
從a~z中找出五個禁止字元
使的wrods中被禁止的字總數最少
'''

def StrArr2BitmapArr(strArr):
    res = []
    for i in range(len(strArr)):
        str = strArr[i]
        bit = 0
        for c in str:
            k = ord(c) - ord('a')
            bit |= (1 << k)
        res.append(bit)
    return res

def GetWordsArr():
    try:
        fin = open('words.txt')
        lt = []
        for line in fin:
            line = line.strip('\n')
            lt.append(line)
        fin.close()
        return lt
    except IOError:
        print(IOerror)
        return lt 

def GetCombArr(srcStr, idx, sltLt, sltNum, dstLt):
    if idx == len(srcStr):
        return

    GetCombArr(srcStr, idx + 1, sltLt, sltNum, dstLt)

    sltLt[sltNum] = srcStr[idx]
    sltNum += 1
    if sltNum == 5:
        dstLt.append(''.join(sltLt.copy()))
    else:
        GetCombArr(srcStr, idx + 1, sltLt, sltNum, dstLt)



import time
tStart = time.time()#計時開始

#建立a-z的所有長度5的組合產生的bitmap
srcStr = "abcdefghijklmnopqrstuvwxyz"
sltLt = [' '] * 5
combArr = []
GetCombArr(srcStr, 0, sltLt, 0, combArr)
combBitmapArr = StrArr2BitmapArr(combArr)

#建立words.txt的所有單字產生的bitmap
wordsArr = GetWordsArr()
wordsBitmapArr = StrArr2BitmapArr(wordsArr)

#初始化最小idx以及最小刪除數量
minIdx = -1
minNum = 2147483647
for i in range(len(combBitmapArr)):
    cnt = 0
    for j in range(len(wordsBitmapArr)):
        if combBitmapArr[i] & wordsBitmapArr[j] > 0:
            cnt += 1
            if(cnt >= minNum):
                break
    if cnt < minNum:
        minNum = cnt
        minIdx = i
    #print(i, combArr[i], cnt)

print(minIdx, combArr[minIdx], minNum)
tEnd = time.time()#計時結束
print (tEnd - tStart)
