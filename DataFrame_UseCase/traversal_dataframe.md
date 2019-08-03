# traversal dataframe


```python
for idx, row in df.iterrows():
    print(idx , type(row))
    
""" result
0 <class 'pandas.core.series.Series'>
10 <class 'pandas.core.series.Series'>
14 <class 'pandas.core.series.Series'>
19064 <class 'pandas.core.series.Series'>
19065 <class 'pandas.core.series.Series'>
19380 <class 'pandas.core.series.Series'>
19879 <class 'pandas.core.series.Series'>
31121 <class 'pandas.core.series.Series'>
"""
```
