'''
<Think Python 習題9-6 Abecedarian 初學者字母 >
	- 從words.txt檔案中找出字母組成順序剛好有嚴格依照英文字母順序排列的所有字,
  - Ex. Almost/ Billowy/ 
	- 重複的雙字母也算, ex. abbccde
'''

def IncreasingWords():
    try:
        lt = []
        fin = open('words.txt')
        cnt = 0
        for str in fin:
            str = str.strip('\n')
            line = str.lower()
            b = True
            for i in range(0, len(line) - 1):
                if line[i] > line[i + 1]:
                    b = False
                    break
            if b == True:
                print(str)
                lt.append(str)
                cnt += 1
        fin.close()
        return lt
    except IOError:
        print(IOerror)
        return lt

IncreasingWords()
