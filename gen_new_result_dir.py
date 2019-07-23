def get_latest_result_dir(parent_dir_name = 'result', child_dir_format = 'result_{0:0>4d}', num = 1):
    """
    gen and get a new dir in the parent dir
    """
    if not os.path.exists(parent_dir_name):
        os.makedirs(parent_dir_name)
    parent_full_dir = os.getcwd() + '\\' + parent_dir_name
    dirs = os.listdir(parent_full_dir)
    print(num, child_dir_format)
    result_dir = child_dir_format.format(num)
    num += 1
    while result_dir in dirs:
        result_dir = child_dir_format.format(num)
        num += 1
    
    result_full_dir = parent_full_dir + '\\' + result_dir
    os.makedirs(result_full_dir)
    
    return result_full_dir
