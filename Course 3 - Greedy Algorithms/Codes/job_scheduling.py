import pandas as pd

def load_data(filepath:str)->list:
    '''
        Load the list of processes and return their number, their weigth and their length.
    '''
    file = open(filepath, 'r')
    lines = file.readlines()
    n_jobs = int(lines[0].strip())
    jobs = [tuple(map(int, x.strip().split(' '))) for x in lines[1:]]
    df_jobs = pd.DataFrame(jobs, columns=['weigth', 'length'])
    assert(len(df_jobs) == n_jobs)
    return df_jobs

def compute_cost(df:pd.DataFrame)->int:
    '''
        Return as cost the sum of the product weigth with length. 
    '''
    cost = 0
    for idx, job in df.iterrows():
        cost += job['weigth'] * df['length'][idx:].sum()
    return cost

def compute_order(df:pd.DataFrame)->(list, list):
    '''
        Compute process order with difference and ratio between their weigth and their length.
    '''
    order_diff = (df['weigth'] - df['length']).sort_values().index.values.astype(int)
    order_ratio = (df['weigth'] / df['length']).sort_values().index.values.astype(int)
    return order_diff, order_ratio

def compute_costs(df:pd.DataFrame)->(int, int, int):
    '''
        Compute costs with several order: unordered, difference and ratio.
    '''
    order_diff, order_ratio = compute_order(df)
    unorder_cost = compute_cost(df)
    diff_cost = compute_cost(df.loc[order_diff])
    ratio_cost = compute_cost(df.loc[order_ratio])
    return unorder_cost, diff_cost, ratio_cost