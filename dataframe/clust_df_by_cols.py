def cluster_df_by_cols(df, cols = []):
    """
    clust dataframe by columns-value and return the list of all dst-df
    
    Return: cluster_df_lt(list)
    """
    cluster_df_lt = []
    unique_value_df = df[cols].drop_duplicates(keep = 'first').reset_index(drop = True)
    for index, row in unique_value_df.iterrows():
        tmp_df = df
        for col_name in cols:
            tmp_df = tmp_df[tmp_df[col_name] == row[col_name]]
        cluster_df_lt.append(tmp_df.reset_index(drop = True))
    return cluster_df_lt

def cluster_df_by_cols2(df, cols = []):
    """
    clust dataframe by columns-value and return the dict of all dst-df
    
    Return: res_dict(dict)
    """
    res_dict = {}
    unique_value_df = df[cols].drop_duplicates(keep = 'first').reset_index(drop = True)
    for index, row in unique_value_df.iterrows():
        tmp_df = df
        key = []
        for col_name in cols:
            key.append(row[col_name])
            tmp_df = tmp_df[tmp_df[col_name] == row[col_name]]
        res_dict[tuple(key)] = tmp_df.reset_index(drop = True)
    return res_dict
