# Get the unique values (rows) of a dataframe in python Pandas

## df.drop_duplicates() 用法

```python
drop_duplicates(subset=None, keep='first', inplace=False) method of pandas.core.frame.DataFrame instance
    Return DataFrame with duplicate rows removed, optionally only
    considering certain columns
    
    Parameters
    ----------
    subset : column label or sequence of labels, optional
        Only consider certain columns for identifying duplicates, by
        default use all of the columns
    keep : {'first', 'last', False}, default 'first'
        - ``first`` : Drop duplicates except for the first occurrence.
        - ``last`` : Drop duplicates except for the last occurrence.
        - False : Drop all duplicates.
    inplace : boolean, default False
        Whether to drop duplicates in place or to return a copy
    
    Returns
    -------
    deduplicated : DataFrame
```

## 範例

```python
import pandas as pd

#Create a DataFrame
d = {
    'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine','Alisa','Bobby','kumar','Alisa','Alex','Cathrine'],
    'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
    'OtherCol':[5,0,0,1,1,0,4,1,1,0,0,0]
}

df = pd.DataFrame(d,columns=['Name','Age','OtherCol'])
```
![](https://i.imgur.com/lzHuKfL.png)


- 取得所有欄位的unique (全部欄位不同才不同)
    ```python
    # keep = 'first', 'last', False
    df1 = df.drop_duplicates(keep = 'first')
    ```
    ![](https://i.imgur.com/v8EagUJ.png)


- 取得特定欄位的unique (指定的欄位不同才不同)
    ```python
    subset = ['Name', 'Age']
    df2 = df.drop_duplicates(subset = subset, keep = 'first')
    ```
    ![](https://i.imgur.com/nxVIws1.png)


- 挑選後看需求可能需要 df.reset_index(drop=True) 
