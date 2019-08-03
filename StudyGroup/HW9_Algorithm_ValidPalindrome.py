import re
import time

"""
pal1用re模組過濾字元，依照我的經驗，python能用包好的function基本效能都不錯
pal2和pal3自己寫逐筆運算，確實比現成的library要來的久

另外比較有意思的是，可以比較test_pals_time1和test_pals_time2的差別
由於pal2不做任何前處理，就直接頭尾互比
所以遇到false case出現在很邊緣的地方，會發現的很快
"""


def pal1(s):
    print(1)
    s1 = re.sub('[^A-Za-z0-9]+', '', s).lower()
    if s1[::-1] == s1:
        return True
    else:
        return False

def pal2(s):
    print(2)
    i = 0
    j = len(s) - 1
    
    while True:
        while i < j and s[i].isalnum() == False:
            i += 1
        while i < j and s[j].isalnum() == False:
            j -= 1
            
        if i < j:
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1   
            else:
                return False
        else:
            return True

def pal3(s):
    print(3)
    lt = []
    for c in s:
        if c.isalnum():
            lt.append(c.lower())
    return lt == lt[::-1]


def get_time(case_num, s, fun):
    start = time.time()
    
    res = fun(s)
    
    end = time.time()
    elapsed = end - start
    print("case%d: Ans = %r, Time taken: %10.8f seconds." %(case_num, res, elapsed))


def test_pals_time1(s = "A man, a plan, a canal: Panama"*100000): 
    # case1
    get_time(1, s, pal1)
    
    # case2
    get_time(2, s, pal2)
    
    # case3
    get_time(3, s, pal3)
    
def test_pals_time2(s = "A man, a plan, a canal: Panama"*100000 + "123"): 
    # case1
    get_time(1, s, pal1)
    
    # case2
    get_time(2, s, pal2)
    
    # case3
    get_time(3, s, pal3)
    