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

    data_series_1 = df.loc[query_metric]
    new_df = pd.DataFrame({'Year':data_series_1.index, 'Value':data_series_1.values})
    result_list = [row.to_dict() for _, row in new_df.iterrows()]

    result_dict = {}
    result_dict['result_data'] = result_list

    return result_dict


# p11 = 'Industry (including construction), value added (constant 2010 US$)'      # IVA
# p12 = 'Manufacturing, value added (constant 2010 US$)'                          # MVA
# p21 = 'Exports of goods and services (current US$)'                             # EGS
# p22 = 'Imports of goods and services (current US$)'                             # IGS
# p31 = 'GDP per capita (constant 2010 US$)'                                      # GDP
# p41 = 'Gross national expenditure (constant LCU)'                               # GNE
# p42 = 'Gross domestic income (constant LCU)'                                    # GDI