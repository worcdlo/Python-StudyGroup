import pandas as pd

"""
參考連結:https://blog.csdn.net/zutsoft/article/details/51498026

merge(left, right, how='inner', on=None, left_on=None, right_on=None,
      left_index=False, right_index=False, sort=True,
      suffixes=('_x', '_y'), copy=True, indicator=False)

- left與right：兩個不同的DataFrame
- how：指的是合併(連接)的方式有inner(內連接),left(左外連接),right(右外連接),outer(全外連接);默認為inner
- on : 指的是用於連接的列索引名稱。必須存在右右兩個DataFrame對像中，如果沒有指定且其他參數也未指定則以兩個DataFrame的列名交集做為連接鍵
- left_on：左則DataFrame中用作連接鍵的列名;這個參數中左右列名不相同，但代表的含義相同時非常有用。
- right_on：右則DataFrame中用作 連接鍵的列名
- left_index：使用左則DataFrame中的行索引做為連接鍵
- right_index：使用右則DataFrame中的行索引做為連接鍵
- sort：默認為True，將合併的數據進行排序。在大多數情況下設置為False可以提高性能
- suffixes：字符串值組成的元組，用於指定當左右DataFrame存在相同列名時在列名後面附加的後綴名稱，默認為('_x','_y')
- copy：默認為True,總是將數據複製到數據結構中；大多數情況下設置為False可以提高性能
- indicator：在 0.17.0中還增加了一個顯示合併數據中來源情況；如只來自己於左邊(left_only)、兩者(both)
"""

time = 'time'
col1 = 'col1'
col2 = 'col2'
col3 = 'col3'
col4 = 'col4'

data1 = {time: ['t1','t2','t3','t4','t5','t6','t7'],
         col1:[1,1,1,2,3,4,5],
         col3:[1,3,1,3,-1,4,5]}

data2 = {time: ['t1','t4','t5','t6','t7','t8','t9'],
         col1:[1,4,3,2,3,4,2],
         col2:[0,0,1,3,0,1,5],
         col4:[0,9,9,9,9,2,2]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print('df1:\n', df1, '\n')
print('df2:\n', df2, '\n')
"""
df1:
   time  col1  col3
0   t1     1     1
1   t2     1     3
2   t3     1     1
3   t4     2     3
4   t5     3    -1
5   t6     4     4
6   t7     5     5 

df2:
   time  col1  col2  col4
0   t1     1     0     0
1   t4     4     0     9
2   t5     3     1     9
3   t6     2     3     9
4   t7     3     0     9
5   t8     4     1     2
6   t9     2     5     2 
"""


# 以df1的'time'為key值，將df1, df2的所有其他col合併成一個df
print("""pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='left')""")
merged_df = pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='left')
print(merged_df, '\n\n')
"""
pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='left')
  time  col1_x  col3  col1_y  col2  col4
0   t1       1     1     1.0   0.0   0.0
1   t2       1     3     NaN   NaN   NaN
2   t3       1     1     NaN   NaN   NaN
3   t4       2     3     4.0   0.0   9.0
4   t5       3    -1     3.0   1.0   9.0
5   t6       4     4     2.0   3.0   9.0
6   t7       5     5     3.0   0.0   9.0 
"""


# 以df1的'col1'為key值，將df1, df2的所有其他col合併成一個df
print("""pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['col1'], how='left')""")
merged_df = pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['col1'], how='left')
print(merged_df, '\n\n')
"""
pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['col1'], how='left')
  time_x  col1  col3 time_y  col2  col4
0     t1     1     1     t1   0.0   0.0
1     t2     1     3     t1   0.0   0.0
2     t3     1     1     t1   0.0   0.0
3     t4     2     3     t6   3.0   9.0
4     t4     2     3     t9   5.0   2.0
5     t5     3    -1     t5   1.0   9.0
6     t5     3    -1     t7   0.0   9.0
7     t6     4     4     t4   0.0   9.0
8     t6     4     4     t8   1.0   2.0
9     t7     5     5    NaN   NaN   NaN 
"""


# 以df1的['time', 'col1']為key值，將df1, df2的所有其他col合併成一個df
print("""pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time', 'col1'], how='left')""")
merged_df = pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time', 'col1'], how='left')
print(merged_df, '\n\n')
"""
pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time', 'col1'], how='left')
  time  col1  col3  col2  col4
0   t1     1     1   0.0   0.0
1   t2     1     3   NaN   NaN
2   t3     1     1   NaN   NaN
3   t4     2     3   NaN   NaN
4   t5     3    -1   1.0   9.0
5   t6     4     4   NaN   NaN
6   t7     5     5   NaN   NaN 
"""


# 以df1的['time', 'col3']為key值，將df1, df2的所有其他col合併成一個df
print("""pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time', 'col3'], how='left')""")
print('[Error] df2 does not has col3\n\n')
# 由於df2沒有col3，會當機
"""
pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time', 'col3'], how='left')
[Error] df2 does not has col3
"""


# right用法同left
# pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='right')


# 以交集的'time'為key值，將df1, df2的所有其他col合併成一個df
print("""pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='inner')""")
merged_df = pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='inner')
print(merged_df, '\n\n')
"""
pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='inner')
  time  col1_x  col3  col1_y  col2  col4
0   t1       1     1       1     0     0
1   t4       2     3       4     0     9
2   t5       3    -1       3     1     9
3   t6       4     4       2     3     9
4   t7       5     5       3     0     9 
"""


# 以聯集的'time'為key值，將df1, df2的所有其他col合併成一個df
print("""pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='outer')""")
merged_df = pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='outer')
print(merged_df, '\n\n')
"""
pd.merge(left=df1, right=df2, left_on=None, right_on=None, on=['time'], how='outer')
  time  col1_x  col3  col1_y  col2  col4
0   t1     1.0   1.0     1.0   0.0   0.0
1   t2     1.0   3.0     NaN   NaN   NaN
2   t3     1.0   1.0     NaN   NaN   NaN
3   t4     2.0   3.0     4.0   0.0   9.0
4   t5     3.0  -1.0     3.0   1.0   9.0
5   t6     4.0   4.0     2.0   3.0   9.0
6   t7     5.0   5.0     3.0   0.0   9.0
7   t8     NaN   NaN     4.0   1.0   2.0
8   t9     NaN   NaN     2.0   5.0   2.0 
"""
