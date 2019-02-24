"""
<Think Python 習題9-3 文字遊戲基本題>
	- 讓使用者輸入一個‘禁止字母’構成的字串
  - 從words.txt檔案中找出所有不含任何禁止字母的字;ex:輸入 bcz, 則要找出的單字不可以含b,c,z
	
  -進階練習
  -從a-z中挑出5個字元當作禁止字母
  -請問哪五個字元可以使的被排除的字最少
"""

#紀錄留下的字數
def Avoids_CntInv(avoidStr):
    try:
        fin = open('words.txt')
        lt = []
        for c in avoidStr:
            if c != '\n' and c != '\r':
                lt.append(c)
        table = set(lt)
        cnt = 0
        for line in fin:
            b = False
            line = line.strip('\n')
            for c in line:
                if c in table:
                    b = True
                    break
            if b is False:
                cnt += 1
                #print(line)
                #time.sleep(0.2)
        fin.close()
        return cnt
    except IOError:
        print(IOerror)
        return -1

#紀錄被排除的字數
def Avoids_Cnt(avoidStr):
    try:
        fin = open('words.txt')
        lt = []
        for c in avoidStr:
            if c != '\n' and c != '\r':
                lt.append(c)
        table = set(lt)
        cnt = 0
        for line in fin:
            line = line.strip('\n')
            for c in line:
                if c in table:
                    cnt += 1
                    break
        fin.close()
        return cnt
    except IOError:
        print(IOerror)
        return -1

#紀錄被排除的字數，若個數>=maxNum，則不用繼續做下去了
def Avoids_Cnt2(avoidStr, maxNum):
    try:
        fin = open('words.txt')
        lt = []
        for c in avoidStr:
            if c != '\n' and c != '\r':
                lt.append(c)
        table = set(lt)
        cnt = 0
        for line in fin:
            line = line.strip('\n')
            for c in line:
                if c in table:
                    cnt += 1
                    break
            if cnt >= maxNum:
                break;
        fin.close()
        return cnt
    except IOError:
        print(IOerror)
        return -1

#紀錄被排除的字數，若個數>=maxNum，則不用繼續做下去了，input換成了事先存進記憶體的list，而不再讀檔
def Avoids_Cnt3(avoidStr, wordsLt, maxNum):
    lt = []
    for c in avoidStr:
        if c != '\n' and c != '\r':
            lt.append(c)
    table = set(lt)

    cnt = 0
    for line in wordsLt:
        for c in line:
            if c in table:
                cnt += 1
                break
        if cnt >= maxNum:
            break;
    return cnt

#將檔案內的文字存成list，配合 Avoids_Cnt3
def GetWords():
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

#列出所有長度5的組合
def Comb(srcStr, idx, sltLt, sltNum, dstLt):
    if idx == len(srcStr):
        return

    Comb(srcStr, idx + 1, sltLt, sltNum, dstLt)

    sltLt[sltNum] = srcStr[idx]
    sltNum += 1
    if sltNum == 5:
        dstLt.append(sltLt.copy())
    else:
        Comb(srcStr, idx + 1, sltLt, sltNum, dstLt)


#找出刪除最少字數的組合
def SmallestComb():
    data = "abcdefghijklmnopqrstuvwxyz"
    sltLt = [' '] * 5
    totalComb = []
    Comb(data, 0, sltLt, 0, totalComb)

    wordsLt = GetWords()
    minNum = 2147483647
    minIdx = -1
    for i in range(len(totalComb)):
        str = ''.join(totalComb[i])
        num = Avoids_Cnt3(str, wordsLt, minNum)
        #num1 = Avoids_Cnt3(str)
        if num < minNum:
            minNum = num
            minIdx = i
        print("idx = %d, removeNum = %d, %s" %(i, num, str));

    if minIdx != -1:
        return totalComb[minIdx]
    return []

ans = SmallestComb()
print("ans = ")
print(ans)
