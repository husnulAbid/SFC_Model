import pandas as pd


dataset_file_name = 'war_effect_data.csv'

def read_dataset(dataset_file_name):
    raw_df = pd.read_csv(f'datasets\{dataset_file_name}', sep = ',', skiprows=2)
    return raw_df


def pre_process_data(df, year_duration):
    del df['Country Name']
    del df['Country Code']
    del df['Indicator Code']

    df = df.dropna()
    df = df.set_index('Indicator Name')

    df = df.iloc[:, 5:5+year_duration] 

    return df


def get_query_data(metric_name, year_duration):
    df = read_dataset(dataset_file_name)
    df = pre_process_data(df, year_duration)
    
    if metric_name == 'GDP':
        query_metric = 'GDP per capita (constant 2010 US$)'
    else:
        query_metric = 'Gross domestic income (constant LCU)'

    result_dict = df.loc[query_metric].to_dict()

    return result_dict