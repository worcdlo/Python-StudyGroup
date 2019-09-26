import pandas as pd

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
