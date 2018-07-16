import pandas as pd
"""
Contains various data utils for pandas dataframes.
"""
def drop_constant_column(dataframe):
    """
    Drops constant value columns of pandas dataframe.
    """
    return dataframe.loc[:, (dataframe != dataframe.iloc[0]).any()]
	
def size_of_data(data):
    print('shape : {} * {}'.format(data.shape[0],data.shape[1]))
    
def data_types(data):
    print('data type : {}'.format(data.dtypes.value_counts().to_dict()))
    
def column_variance(data,threshold=1.0):
    variance = data.var().sort_values()
    return variance[variance<=threshold]

def column_range(data):
    return (data.max()-data.min()).sort_values(ascending=False)

def column_counts(data):
    return data.nunique().sort_values(ascending=False)	